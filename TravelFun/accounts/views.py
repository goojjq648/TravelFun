from .models import Member  # 引入會員模型
from .forms import MemberEditForm, LoginForm, MemberForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import MemberEditForm, MemberRegistrationForm, LoginForm, MemberForm
from .forms import MemberRegistrationForm

from .auth import authenticate_member  # 自定義的身份驗證函式
from .forms import MemberRegistrationForm
# 確保用戶是管理員才能查看會員列表
def is_admin(member):
    return member.level == 'admin'

# 搜尋會員
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
        form = MemberRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '註冊成功！')
            return redirect('login')
    else:
        form = MemberRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})
# 會員編輯視圖
def edit_member(request, id):
    member = get_object_or_404(Member, id=id)
    if request.method == 'POST':
        form = MemberEditForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, '會員資訊已更新！')
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

# 登入視圖
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # 重置 session，確保之前的會話被清除
            request.session.flush()

            member = authenticate_member(username, password)
            if member:
                # 登入成功，保存 session
                request.session['member_id'] = member.id
                request.session['member_level'] = member.level  # 保存會員等級
                request.session['full_name'] = member.full_name  # 保存會員全名
                return redirect('member_list')
            else:
                messages.error(request, '登入失敗，帳號或密碼不正確')
        else:
            messages.error(request, '表單無效')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


# 登出視圖
def logout_view(request):
    # 清除 session
    request.session.flush()
    messages.success(request, '登出成功！')
    return redirect('login')  # 返回登入頁面


def dashboard(request):
 
    return render(request, 'dashboard.html')  