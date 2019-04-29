


class Expt_Info:
    # 专家信息类
    # eid 专家编号
    # ins 机构列表
    # modifyExptInfo 修改专家信息(kind, content)   //修改专家信息，kind对应要修改的部分，content对应修改后的内容
    # bool 管理科研成果(kind)    //kind表示具体的操作类型（增加、删除、修改），返回值表示操作是否成功

    # 构造函数，expt_id为专家编号，ins为专家的科研机构编号列表
    # user_id为专家信息对应的用户的用户id, intro为专家介绍
    def __init__(self, eid = 0, institution = [], uid = None, introduction = ''):
        self.expt_id = eid
        self.ins = institution
        self.user_id = uid
        self.intro = introduction

    # 管理科研成果 kind 表示对应的操作类型
    def manageAchievements(self, kind):
        result = 0 #1表示操作成功
        if kind == 0:# 0 对应添加科研成果
            print("add")
            result = 1
        elif kind == 1:# 1 对应删除科研成果
            print("delete")
            result = 1
        elif kind == 2:  # 2 对应修改科研成果
            print("modify")
            result = 1

        return result

    # 修改专家信息 kind表示要修改的内容(0 表示修改专家介绍， 1 表示修改科研机构)
    def modifyExptInfo(self, kind, content):
        if kind == 0:
            self.intro = content
        elif kind == 1:
            self.ins = content
        else :
            print('nothing changes')




