# Shared platform of technical research source
接口说明
收藏:Like
#接受收藏成果
def create_like(request,resource_id), 参数其实为前端向后端传参得到
#取消收藏成果
def delete_like(request,resource_id):, 参数其实为前端向后端传参得到
#接受收藏专家
def create_like_expert(request,expert_id):, 参数其实为前端向后端传参得到
#取消收藏
def delete_like_expert(request,expert_id):, 参数其实为前端向后端传参得到

通知 Notification
#创建评论被举报的通知
#通知用户，他的评论被人举报
def create_notofication_report_comment(request,commentuserid,commentid):
#阅读了评论相关举报消息
def read_comment_report(request,notification_id):
#阅读了科技成果相关的举报消息
def read_SciAchi_report(request,notification_id):
#阅读了专家相关的举报消息
def read_expert_report(request,notification_id):
#删除评论被举报的消息
def delete_comment_report(request,notification_id):
#删除科技成果相关的举报消息
def delete_SciAchi_report(request,notification_id):
#删除专家相关的举报消息
def delete_expert_report(request,notification_id):
#通知用户，被举报的评论已经被管理员删除
#通知举报人：你的举报已通过
#通知评论人：你的评论已经被删除
#user_id 是举报人的id
def reported_comment_delete(request,Comment_id,user_id):
#通知用户，被举报的评论未被管理员认可，仍旧保留
#通知举报人：你的举报已被驳回
#通知评论人：你的评论仍旧保留
#user_id 是举报人的id
def reported_comment_delete(request,Comment_id,user_id):
#通知举报人，他所举报的科技资源错误已经被管理员修复
#user_id为举报人id
def agree_SciAchi_report_agree(request,resource_id,user_id):
#通知举报人，他所举报的科技资源错误已经被管理员删除
#user_id为举报人id
def agree_SciAchi_report_delete(request,resource_id,user_id):
#通知举报人，他的举报成果被驳回
def notagree_SciAchi_report(request, resource_id,user_id):
#通知举报人，他举报的专家信息已经被管理员修复
def agree_expert_report_agree(request,expert_id,user_id):
#通知举报人，他所举报的专家错误已经被管理员删除
#user_id为举报人id
def agree_SciAchi_report_delete(request,expert_id,user_id):
#通知举报用户，他对于专家的举报已经被驳回
def notagree_SciAchi_report(request,expert_id,user_id):


举报 Report
#举报某成果
def create_report(request,resource_id):
#举报某专家
def create_report_expert(request,expert_id):
#展示成果类的未处理举报信息
def show_resource_report_not(request):
#展示成果类的已处理举报信息
def show_resource_report_ok(request):
#展示专家类的未处理举报信息
def show_expert_report_not(request):
#展示专家类的已处理举报信息
def show_resource_expert_ok(request):
#展示已处理评论举报
def show_resource_comment_ok(request):
#展示未处理评论举报
def show_comment_report_not(request):
#处理成果类举报通过(修改）
def agree_resource_report(request,report_id):
#处理成果类举报通过(删除）
def agree_resource_report_delete(request,report_id):
#处理成果类举报不通过
def notagree_resource_report(request,report_id):
#处理专家类举报通过（修改）
def agree_expert_report(request,report_id):
#处理专家类举报通过（删除）
def agree_expert_report_delete(request,report_id):
#处理专家类举报不通过
def notagree_expert_report(request,report_id):
#处理评论类举报通过
def agree_comment_report(request,report_id):
#处理评论类举报不通过
def not_agree_comment_report(request,report_id):

科技成果 TechResource
#展示所有在数据库中的论文
def list_all(request):
#展示一个指定了resource_id的论文
#包括论文数据和评论数据
def list_one(self,request,resource_id):
#上传一个科技成果
!待修改 上传文件生成url
def create(request):

用户 User
#用户登录
def login(request):
#用户注册
def register(request):
#用户注册验证
def make_confirm_string(NormalUser):
#发送验证邮件
def send_email(email, code):
#用户登出
def logout(request):
#普通用户主页展示信息
def show_user(request):
#专家主页展示
def show_expert(request,expert_id):
#专家成果搜索
#专家词云

评论 UserComment
#创建评论
def create_comment(request,resource_id):参数其实为前端向后端传参得到
#删除评论
def delete_comment(request,Comment_id):

访问历史：VisitHistory
#增加资源类访问记录
def add_visit_resource_history(request,resource_id):
#增加专家类访问记录
def add_visit_expert_history(request,expert_id):

申请 Apply
#列出所有的未处理的创建成为专家的申请
def not_done_applytoexpert(request):
#列出所有的已处理的创建成为专家的申请
def not_done_applytoexpert(request):
#创建新的成为专家申请
def apply_to_expert(request):
#创建专家认领申请
def verification_to_expert(request,expert_id):

#普通用户提交申请
#显示未处理申请
#显示已处理申请
#管理员通过申请（与通知相连）
#管理员驳回申请（与通知相连）
#显示某用户的申请

词云 wordcloud
#根据访问历史获得词云
#词云+检索接口
