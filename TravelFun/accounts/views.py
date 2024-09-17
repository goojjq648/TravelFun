
from .models import Member  # 假設你已經創建了會員資料表 Member
from .forms import MemberEditForm
from django.shortcuts import render, get_object_or_404, redirect
from .forms import MemberForm
from django.contrib import messages
from .models import Member
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, MemberEditForm
from .forms import LoginForm, RegistrationForm, MemberEditForm
from django.db.models import Q
from .auth import authenticate_member  # 自定義的身份驗證函式



# 確保用戶是管理員才能查看會員列表
# 判斷是否為管理者
def is_admin(member):
    return member.level == 'admin'

#搜尋會員
def search_members(request):
    query = request.GET.get('search')
    if query:
        members = Member.objects.filter(
            Q(full_name__icontains=query) | Q(username__icontains=query)
        )
    else:
        members = Member.objects.all()

    return render(request, 'accounts/member_list.html', {'members': members})




def member_list(request):
    member_id = request.session.get('member_id')
    if not member_id:
        return redirect('login')  # 未登入，重定向到登入頁面

    member = Member.objects.get(id=member_id)
    if member.level != 'admin':  # 確認會員等級是否為管理員
        return redirect('no_permission')  # 如果不是管理員，重定向到無權限頁面

    members = Member.objects.all()
    return render(request, 'accounts/member_list.html', {'members': members})

# 新增用戶
def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '會員新增成功！')
            return redirect('member_list')  # 新增成功後重定向到會員列表
    else:
        form = MemberForm()
    
    return render(request, 'accounts/add_member.html', {'form': form})


# 註冊視圖
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.level = 'user'  # 新用戶預設為 user
            member.set_password(form.cleaned_data['password'])  # 設置密碼
            member.save()

            messages.success(request, '註冊成功！')

            # 自動登入
            if authenticate_member(request, member.username, form.cleaned_data['password']):
                request.session['member_id'] = member.id
                return redirect('member_list')
            else:
                messages.error(request, '登入失敗，請使用正確的帳號和密碼')
        else:
            messages.error(request, '註冊表單無效，請檢查輸入的內容')
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})




# 會員編輯視圖
def edit_member(request, id):
    member = get_object_or_404(Member, id=id)
    if request.method == 'POST':
        form = MemberEditForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberEditForm(instance=member)
    return render(request, 'accounts/edit_member.html', {'form': form})

# 刪除會員視圖
def delete_member(request, id):
    
    member = get_object_or_404(Member, id=id)
    if request.method == 'POST':
        member.delete()
        return redirect('member_list')
    return render(request, 'accounts/confirm_delete.html', {'member': member})



# 無權限視圖
def no_permission(request):
    return render(request, 'accounts/no_permission.html')


def delete_member_view(request, id):
    # 確保從 session 中獲取當前會員的 ID
    member_id = request.session.get('member_id')
    if not member_id:
        return redirect('login')

    member = Member.objects.get(id=member_id)
    if member.level != 'admin':
        messages.error(request, '您沒有權限刪除此會員！')
        return redirect('member_list')

    member_to_delete = get_object_or_404(Member, id=id)
    member_to_delete.delete()
    messages.success(request, '會員已成功刪除！')
    return redirect('member_list')



@login_required



def dashboard(request):
    if request.user.member.level in ['admin', 'editor']:
        members = Member.objects.all()
        return render(request, 'members.html', {'members': members})
    return redirect('home')



# 登入視圖
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            member = authenticate_member(username, password)
            if member:
                # 登入成功，保存 session
                request.session['member_id'] = member.id
                request.session['member_level'] = member.level  # 保存會員等級
                messages.success(request, '登入成功！')
                return redirect('member_list')
            else:
                messages.error(request, '登入失敗，帳號或密碼不正確')
        else:
            messages.error(request, '表單無效')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

# 會員列表視圖
def member_list(request):
    member_level = request.session.get('member_level')

    if member_level == 'admin':
        members = Member.objects.all()
        return render(request, 'accounts/member_list.html', {'members': members})
    else:
        return redirect('no_permission') 



def dashboard_view(request):
    user = request.user  # 獲取當前的用戶
    if hasattr(user, 'member'):
        if user.member.level == 'admin':
            members = Member.objects.all()
            return render(request, 'members.html', {'members': members})
        elif user.member.level == 'editor':
            members = Member.objects.all()  # 根據會員等級篩選
            return render(request, 'members.html', {'members': members})
        else:
            return redirect('home')  # 普通會員不能查看會員列表
    return redirect('home')

# 登出視圖
def logout_view(request):
    # 清除 session
    request.session.flush()
    messages.success(request, '登出成功！')
    return redirect('login')  # 返回登入頁面


