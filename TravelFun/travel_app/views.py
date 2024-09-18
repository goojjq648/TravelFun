
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, FileResponse
from .models import Travel,Taiwen,Counties,TravelClass
from datetime import datetime
import time
import json
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def travel_main(request):
    if request.method == 'POST':
        travelName = request.POST.get('name')
        if travelName:
            travel = Travel.objects.filter(travel_name__icontains=travelName)
            return render(request, 'travel/travel.html', {"travel":travel})

    travel = Travel.objects.all()
    return render(request, 'travel/travel.html', {"travel":travel})


def register(request):
    
    return render(request, 'travel/register.html')

def edit(request, id):   
    travel = Travel.objects.get(travel_id=id)  
    return render(request, 'travel/edit.html',{'travel': travel})

#新增資料
def register01(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        txt = request.POST.get('txt')
        tel = request.POST.get('tel')
        address = request.POST.get('address')
        region = request.POST.get("region")
        town = request.POST.get('town')
        linginfo = request.POST.get('linginfo')
        opentime = request.POST.get('opentime')
        image1 = request.POST.get('image1')
        image2 = request.POST.get('image2')
        image3 = request.POST.get('image3')
        Px = request.POST.get('Px')
        Py = request.POST.get('Py')
        website = request.POST.get('website')
        tickinfo = request.POST.get('tickinfo')
        parkinfo = request.POST.get('parkinfo')

        #景點屬性

        class_list = request.POST.getlist("class")
        if not class_list:
            return HttpResponse("您好，請至少選一個類別", 'text/plain')
        class1=class_list[0]
        if len(class_list)>=2:
            class2=class_list[1]
        else:
            class2=None
        if len(class_list)>=3:
            class3=class_list[2]
        else:
            class3=None
    #確認資料是否是NULL
    if not name:
       return HttpResponse("您好，景點名稱不能是空的", 'text/plain')
    if not Px or not Py :
        return HttpResponse("您好，經/緯度不能是空的", 'text/plain')
    if Travel.objects.filter(travel_name=name):
       return HttpResponse("您好，景點名稱已註冊", 'text/plain')
    if not region or not town:
        return HttpResponse("您好，縣市/鄉鎮市(區)欄位不能為空", 'text/plain')
    
    #確認資料是否存在
    if tel and Travel.objects.filter(tel=tel):
       return HttpResponse("您好，此電話已註冊", 'text/plain')
    if address and Travel.objects.filter(travel_address=address):
       return HttpResponse("您好，此地址已註冊", 'text/plain')
    if not Counties.objects.filter(name=region):
        return HttpResponse("您好，此縣市不存在", 'text/plain')
    if not Taiwen.objects.filter(region=region,town=town) :
        return HttpResponse("您好，這縣市，不存在此鄉鎮市", 'text/plain')
    
    
    # 把檔案寫進uploads資料夾
    uploaded_file = request.FILES.get('avator')
    if uploaded_file:
       fs = FileSystemStorage()
       file_name = fs.save(uploaded_file.name, uploaded_file)
    
    Travel.objects.create(
        travel_name = name,
        travel_txt = txt,
        tel = tel,
        travel_address = address,
        region = region,
        town = town,
        travel_linginfo =linginfo,
        opentime = opentime,
        image1 = image1,
        image2 = image2,
        image3 = image3,
        px = Px,
        py = Py,
        class1_id = class1,
        class2_id = class2,
        class3_id = class3,
        website = website,
        ticketinfo = tickinfo,
        parkinginfo = parkinfo,
        upload = datetime.now()
    )
    content =  f"您好，景點:{name}，已加入資料庫  "
    return HttpResponse(content, 'text/plain')

def edit01(request,id):
    travel = Travel.objects.get(travel_id=id) 
    if request.method == 'POST':
        #輸入名字
        if travel.travel_name != request.POST.get('name'):
            if Travel.objects.filter(travel_name=request.POST.get('name')):
                return HttpResponse("您好，景點名稱已註冊", 'text/plain')
            else:
                travel.travel_name = request.POST.get('name')
        
        travel.travel_txt = request.POST.get('txt')
        #輸入電話
        if travel.tel != request.POST.get('tel'):
            if travel.tel and Travel.objects.filter(tel=travel.tel):
                return HttpResponse("您好，此電話已註冊", 'text/plain')
            else :
                travel.tel = request.POST.get('tel')

        #輸入地址
        if travel.travel_address != request.POST.get('address'):
            if travel.travel_address and Travel.objects.filter(travel_address=travel.travel_address):
                return HttpResponse("您好，此地址已註冊", 'text/plain')
            else :
                travel.travel_address = request.POST.get('address')
        travel.region = request.POST.get("region")
        travel.town = request.POST.get('town')
        travel.travel_linginfo = request.POST.get('linginfo')
        travel.opentime = request.POST.get('opentime')
        travel.image1 = request.POST.get('image1')
        travel.image2 = request.POST.get('image2')
        travel.image3 = request.POST.get('image3')
        travel.px = request.POST.get('Px')
        travel.py = request.POST.get('Py')
        travel.website = request.POST.get('website')
        travel.ticketinfo = request.POST.get('tickinfo')
        travel.parkinginfo = request.POST.get('parkinfo')

        #景點屬性
        if not request.POST.getlist("class"):
            return HttpResponse("您好，請至少選一個類別", 'text/plain')
        class1 = TravelClass.objects.get(class_id=request.POST.getlist("class")[0])
        travel.class1=class1
        if len(request.POST.getlist("class"))>=2:
            class2 = TravelClass.objects.get(class_id=request.POST.getlist("class")[1])
            travel.class2=class2
        if len(request.POST.getlist("class"))>=3:
            class3 = TravelClass.objects.get(class_id=request.POST.getlist("class")[2])
            travel.class3=class3

    #確認資料是否是NULL
    if not travel.travel_name:
       return HttpResponse("您好，景點名稱不能是空的", 'text/plain')
    if not travel.px or not travel.py :
        return HttpResponse("您好，經/緯度不能是空的", 'text/plain')
    if not travel.region or not travel.town:
        return HttpResponse("您好，縣市/鄉鎮市(區)欄位不能為空", 'text/plain')
    
    #確認資料是否存在
    
    if not Counties.objects.filter(name=travel.region):
        return HttpResponse("您好，此縣市不存在", 'text/plain')
    if not Taiwen.objects.filter(region=travel.region,town=travel.town) :
        return HttpResponse("您好，這縣市，不存在此鄉鎮市", 'text/plain')
    
    
    # 把檔案寫進uploads資料夾
    uploaded_file1 = request.FILES.get('image1')
    uploaded_file2 = request.FILES.get('image2')
    uploaded_file3 = request.FILES.get('image3')

    if uploaded_file1:
       fs = FileSystemStorage()
       travel.image1 = fs.save(uploaded_file1.name, uploaded_file1)
    if uploaded_file2:
       fs = FileSystemStorage()
       travel.image2 = fs.save(uploaded_file2.name, uploaded_file2)
    if uploaded_file3:
       fs = FileSystemStorage()
       travel.image3 = fs.save(uploaded_file3.name, uploaded_file3)

    travel.save()
    content =  f"您好，景點資訊，已修改  "
    return HttpResponse(content, 'text/plain')
    


#刪除資料
def delete(request, id):   
    todo = Travel.objects.get(travel_id=id)  
    todo.delete()
    return redirect('travel:travel')

#預覽資料
def preview(request,id):
    travel = Travel.objects.get(travel_id=id) 
    classes = TravelClass.objects.all()

    return render(request,"travel/preview.html",{'travel': travel})


#讀取縣市資料
def region(request):
    regions = Counties.objects.values('name').distinct()
    regions = [item['name'] for item in regions]
    return JsonResponse(regions, safe=False)

#讀取鄉鎮市區資料
def town(request, region_name): 
    towns = Taiwen.objects.filter(region=region_name).values('town')
    towns = [item['town'] for item in towns]
    return JsonResponse(towns, safe=False)

#顯示篩選資料
def show(request, town_name):
    travels = Travel.objects.filter(town = town_name).values()
    print(travels)
    travels = [item for item in travels]
    print(travels)
    return JsonResponse(travels, safe=False)

#確認景點名稱
def travelName(request):
    name = request.GET.get("name")
    result = {
        "name_exists": False,
    }
    if Travel.objects.filter(travel_name=name).exists():
        result["name_exists"] = True
    return JsonResponse(result, safe=False)

#確認電話
def travelTel(request):
    tel = request.GET.get("tel")
    result = {
        "tel_exists": False,
    }
    if Travel.objects.filter(tel=tel).exists():
        result["tel_exists"] = True
    return JsonResponse(result, safe=False)

#確認地址
def travelAddress(request):
    address = request.GET.get("address")
    result = {
        "address_exists": False,
    }
    if Travel.objects.filter(travel_address=address).exists():
        result["address_exists"] = True
    return JsonResponse(result, safe=False)

#確認縣市
def travelRegion(request):
    region = request.GET.get("region")
    result = {
        "region_exists": False,
    }
    if Counties.objects.filter(name=region).exists():
        result["regoin_exists"] = False
    return JsonResponse(result, safe=True)

#確認鄉鎮市區
def travelTown(request):
    town = request.GET.get("town")
    result = {
        "town_exists": False,
    }
    if Taiwen.objects.filter(town=town).exists():
        result["town_exists"] = False
    return JsonResponse(result, safe=False)