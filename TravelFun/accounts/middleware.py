class MemberMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 將 member_id 加入 request 物件
        request.member_id = request.session.get('member_id')
        response = self.get_response(request)
        return response
