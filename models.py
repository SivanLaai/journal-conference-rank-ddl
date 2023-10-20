# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class CRUD(db.Model):
    __tablename__ = 'CRUD'

    id = db.Column(db.Integer, primary_key=True, info='操作id')
    value = db.Column(db.String(30), server_default=db.FetchedValue(), info='操作值')
    name = db.Column(db.String(30), server_default=db.FetchedValue(), info='操作名称')



class Conference(db.Model):
    __tablename__ = 'Conference'

    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(255))
    other_name = db.Column(db.String(255))
    home_link = db.Column(db.String(255))
    ccf = db.Column(db.String(255))
    dblp = db.Column(db.String(255))
    full_name = db.Column(db.String(255))
    sub = db.Column(db.String(255))
    remark = db.Column(db.String(1000))



class ConferenceDetail(db.Model):
    __tablename__ = 'ConferenceDetail'

    id = db.Column(db.String(50), primary_key=True, nullable=False)
    year = db.Column(db.Integer, primary_key=True, nullable=False)
    conference_link = db.Column(db.String(255))
    timezone = db.Column(db.String(255))
    abstract_deadline = db.Column(db.String(255))
    deadline = db.Column(db.DateTime)
    place = db.Column(db.String(255))
    date = db.Column(db.DateTime)
    acceptance_rate = db.Column(db.Float)
    remark = db.Column(db.String(1000))



class Construction(db.Model):
    __tablename__ = 'Construction'

    id = db.Column(db.String(20), primary_key=True, info='身份证 护照')
    name = db.Column(db.String(100, 'utf8mb4_bin'), info='姓名')
    phone = db.Column(db.String(20), info='手机号')
    email = db.Column(db.String(50), info='用户邮箱')
    district_id = db.Column(db.Integer, info='所属校区ID')
    district_name = db.Column(db.String(100), info='所属校区名称')
    project_id = db.Column(db.Integer, info='所属项目id')
    position = db.Column(db.String(20), info='人员职务')
    resident = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否住校（0代表是 1代表否）')
    resident_district_address = db.Column(db.String(100), server_default=db.FetchedValue(), info='住宿的详情地址')
    is_not_school = db.Column(db.String(100), info='是否在校')
    resident_district_id = db.Column(db.String(25), info='住宿校区id')



class ConstructionProject(db.Model):
    __tablename__ = 'ConstructionProject'

    id = db.Column(db.Integer, primary_key=True, info='基建项目组id')
    name = db.Column(db.String(255), info='项目组名称')



class Dept(db.Model):
    __tablename__ = 'Dept'

    id = db.Column(db.Integer, primary_key=True, info='部门id')
    parent_id = db.Column(db.Integer, server_default=db.FetchedValue(), info='父部门id')
    name = db.Column(db.String(30), nullable=False, server_default=db.FetchedValue(), info='部门名称')
    code = db.Column(db.String(30), info='国科大单位代码')
    other_names = db.Column(db.String(100), info='别名')



class DeptGroup(db.Model):
    __tablename__ = 'DeptGroup'

    dept_id = db.Column(db.String(20), nullable=False, info='部门ID')
    group_id = db.Column(db.Integer, nullable=False, info='用户组ID')
    id = db.Column(db.Integer, primary_key=True)



class District(db.Model):
    __tablename__ = 'District'

    id = db.Column(db.Integer, primary_key=True, info='校区id')
    name = db.Column(db.String(30), server_default=db.FetchedValue(), info='校区名称')
    address = db.Column(db.String(30), server_default=db.FetchedValue(), info='校区地址')



class Group(db.Model):
    __tablename__ = 'Group'

    id = db.Column(db.Integer, primary_key=True, info='老师组ID')
    parent_id = db.Column(db.Integer, server_default=db.FetchedValue(), info='父老师组ID')
    name = db.Column(db.String(256), nullable=False, info='老师组名字')



class GroupRole(db.Model):
    __tablename__ = 'GroupRole'

    group_id = db.Column(db.Integer, nullable=False, info='用户组ID')
    role_id = db.Column(db.Integer, nullable=False, info='角色ID')
    id = db.Column(db.Integer, primary_key=True)



class Health(db.Model):
    __tablename__ = 'Health'

    id = db.Column(db.String(20), primary_key=True, info='身份证或者护照号\r\n')
    name = db.Column(db.String(255), info='姓名')
    institute_id = db.Column(db.Integer, info='研究所id')
    dept_id = db.Column(db.Integer, info='部门id')
    school_id = db.Column(db.Integer, info='学院id')
    district_id = db.Column(db.Integer, info='所属校区')
    type = db.Column(db.Integer, server_default=db.FetchedValue(), info='0 - 教职工，1 - 学生，2 - 后勤人员，3 - 基建人员，4 - 其他人员')
    health_code = db.Column(db.Integer, info='健康宝状态')
    acid_check_day = db.Column(db.Integer, info='核酸检测天数')
    check_result = db.Column(db.Integer, info='检查结果 0,1 阴 2 阳 3 等待结果')
    check_time = db.Column(db.DateTime, server_default=db.FetchedValue(), info='检测时间')
    first_vaccine_time = db.Column(db.DateTime, info='第一剂疫苗时间')
    first_vaccine_manufacturer = db.Column(db.String(255), info='第一剂疫苗厂商')
    second_vaccine_time = db.Column(db.DateTime, info='第二剂疫苗时间')
    second_vaccine_manufacturer = db.Column(db.String(255), info='第二剂疫苗厂商')
    third_vaccine_time = db.Column(db.DateTime, info='第三剂疫苗时间')
    third_vaccine_manufacturer = db.Column(db.String(255), info='第三剂疫苗厂商')
    project_id = db.Column(db.Integer, info='所属项目')
    status = db.Column(db.Integer, server_default=db.FetchedValue(), info='核酸检测是否符合标准 0 - 异常 1 - 正常')
    update_active = db.Column(db.Integer, info='是否开启更新核酸信息  1 - 开启  0 - 不开启')
    acid_frequency_label_id = db.Column(db.Integer, info='核酸频次标签id')



class HealthAcidFrequencyLabel(db.Model):
    __tablename__ = 'HealthAcidFrequencyLabel'

    id = db.Column(db.Integer, primary_key=True, info='核酸频次标签id')
    name = db.Column(db.String(255), info='核酸频次标签名称')



t_HealthAcidLabelmiddle = db.Table(
    'HealthAcidLabelmiddle',
    db.Column('id', db.String(25), nullable=False, info='身份证号 护照'),
    db.Column('acid_frequency_label_id', db.Integer, nullable=False, info='标签'),
    db.Index('HealthAcidLabelmiddle_UN', 'id', 'acid_frequency_label_id')
)



class HealthAcidSetting(db.Model):
    __tablename__ = 'HealthAcidSetting'

    id = db.Column(db.String(20), primary_key=True, info='身份证号')
    check_start_time = db.Column(db.DateTime, info='配置开始时间')
    check_end_time = db.Column(db.DateTime, info='配置结束时间')
    create_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    health_label_id = db.Column(db.Integer, info='核酸频次配置标签id')



class HealthHistory(db.Model):
    __tablename__ = 'HealthHistory'
    __table_args__ = (
        db.Index('HealthHistory_UN', 'check_time', 'id'),
    )

    id = db.Column(db.String(20), primary_key=True, nullable=False, info='身份证或者护照号\r\n')
    health_code = db.Column(db.Integer, info='健康码状态')
    check_result = db.Column(db.Integer, info='检测结果')
    check_time = db.Column(db.DateTime, primary_key=True, nullable=False, server_default=db.FetchedValue(), info='检测时间')



class HealthLabel(db.Model):
    __tablename__ = 'HealthLabel'

    id = db.Column(db.Integer, primary_key=True, info='核酸频次标签id')
    name = db.Column(db.String(255), info='配置名字 由检测天数和次数生成')
    check_days = db.Column(db.Integer, info='检测天数')
    check_times = db.Column(db.Integer, info='检测次数')
    is_default = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否为默认的配置  1 - 是 否 - 0， 默认为0，且只能有一个为1 ')



class Institute(db.Model):
    __tablename__ = 'Institute'

    id = db.Column(db.Integer, primary_key=True, info='研究所id')
    name = db.Column(db.String(30), server_default=db.FetchedValue(), info='研究所名称')
    code = db.Column(db.String(30), info='国科大单位代码')
    address = db.Column(db.String(255), info='研究所地址')



class InstituteGroup(db.Model):
    __tablename__ = 'InstituteGroup'

    institute_id = db.Column(db.String(20), nullable=False, info='部门ID')
    group_id = db.Column(db.Integer, nullable=False, info='用户组ID')
    id = db.Column(db.Integer, primary_key=True)



class Journal(db.Model):
    __tablename__ = 'Journal'

    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    ccf = db.Column(db.String(255))
    jcr = db.Column(db.String(255))
    cas = db.Column(db.String(255))
    _if = db.Column('if', db.String(255))
    full_name = db.Column(db.String(255))
    dblp = db.Column(db.String(255))
    home_link = db.Column(db.String(255))
    submission = db.Column(db.String(255))
    page_number = db.Column(db.Integer)
    acceptance_rate = db.Column(db.Float)
    review_duration = db.Column(db.Float)
    remark = db.Column(db.String(1000))



class Logistic(db.Model):
    __tablename__ = 'Logistics'

    id = db.Column(db.String(20), primary_key=True, info='身份证 护照')
    name = db.Column(db.String(100), info='姓名')
    company_name = db.Column(db.String(100), info='公司类型')
    phone = db.Column(db.String(20), info='手机号')
    email = db.Column(db.String(50), info='用户邮箱')
    label = db.Column(db.String(20), info='冷链、快递、维修、保安、食堂、保洁、商户、物业、楼管、公寓、其他')
    type = db.Column(db.Integer, server_default=db.FetchedValue(), info='在编-0、劳务派遣-0')
    district_id = db.Column(db.Integer, info='所属校区ID')
    institute_id = db.Column(db.Integer, info='所属研究所ID')
    resident = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否住校（0代表是 1代表否）')
    resident_district_id = db.Column(db.Integer, server_default=db.FetchedValue(), info='住宿的校区id')
    resident_district_address = db.Column(db.Integer, server_default=db.FetchedValue(), info='住宿的详情地址')
    dept_id = db.Column(db.Integer, info='所属总务后勤部门id')
    head_teacher_id = db.Column(db.String(20), info='负责人 老师ID')
    head_teacher_name = db.Column(db.String(20), info='负责人名字')
    sex = db.Column(db.Integer, info='用户性别（0男 1女 2未知）')
    del_flag = db.Column(db.Integer, server_default=db.FetchedValue(), info='删除标志（0代表存在 1代表删除）')
    avatar = db.Column(db.String(100), info='头像路径')
    remark = db.Column(db.String(500), info='备注')



class Menu(db.Model):
    __tablename__ = 'Menu'

    id = db.Column(db.Integer, primary_key=True, info='菜单ID')
    title = db.Column(db.String(255), info='菜单名称')
    title_en = db.Column(db.String(255), info='英文菜单名称')
    parent_id = db.Column(db.Integer, info='父菜单ID')
    img = db.Column(db.String(255))
    img1 = db.Column(db.String(255))
    path = db.Column(db.String(200), server_default=db.FetchedValue(), info='请求地址')
    menu_type = db.Column(db.Integer, info='菜单类型（0,侧菜单栏 1,右侧菜单）')
    visible = db.Column(db.Integer, server_default=db.FetchedValue(), info='菜单状态（1显示 2隐藏）')
    icon = db.Column(db.String(100), server_default=db.FetchedValue(), info='菜单图标')
    remark = db.Column(db.String(500), server_default=db.FetchedValue(), info='备注')



class Other(db.Model):
    __tablename__ = 'Other'

    id = db.Column(db.Integer, primary_key=True, info='非教职工人员组id')
    name = db.Column(db.String(30), server_default=db.FetchedValue(), info='非教职工人员组名称')
    remark = db.Column(db.String(255), info='备注')



class Role(db.Model):
    __tablename__ = 'Role'

    id = db.Column(db.Integer, primary_key=True, info='角色ID')
    name = db.Column(db.String(30), nullable=False, info='角色名称')
    parent_id = db.Column(db.Integer, info='父角色ID，会继承来自父亲的所有权限')
    active = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='角色状态（0正常 1停用）')
    create_by = db.Column(db.String(64), server_default=db.FetchedValue(), info='创建者')
    created_at = db.Column(db.DateTime, server_default=db.FetchedValue(), info='创建时间')
    update_by = db.Column(db.String(64), server_default=db.FetchedValue(), info='更新者')
    updated_at = db.Column(db.DateTime, server_default=db.FetchedValue(), info='更新时间')
    remark = db.Column(db.String(500), info='备注')



class RoleCRUD(db.Model):
    __tablename__ = 'RoleCRUD'

    role_id = db.Column(db.Integer, nullable=False, info='角色ID')
    crud_id = db.Column(db.Integer, nullable=False, info='操作id')
    id = db.Column(db.Integer, primary_key=True)



class RoleDept(db.Model):
    __tablename__ = 'RoleDept'

    role_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='角色ID')
    dept_id = db.Column(db.Integer, nullable=False, info='部门ID')
    id = db.Column(db.Integer, primary_key=True)



class RoleDistrict(db.Model):
    __tablename__ = 'RoleDistrict'

    role_id = db.Column(db.Integer, nullable=False, info='角色ID')
    district_id = db.Column(db.Integer, nullable=False, info='院系ID')
    id = db.Column(db.Integer, primary_key=True)



class RoleInstitute(db.Model):
    __tablename__ = 'RoleInstitute'

    role_id = db.Column(db.Integer, nullable=False, info='角色ID')
    institute_id = db.Column(db.Integer, nullable=False, info='院系ID')
    id = db.Column(db.Integer, primary_key=True)



class RoleMenu(db.Model):
    __tablename__ = 'RoleMenu'

    role_id = db.Column(db.Integer, nullable=False, info='角色ID')
    menu_id = db.Column(db.Integer, nullable=False, info='菜单ID')
    id = db.Column(db.Integer, primary_key=True)



class RoleOther(db.Model):
    __tablename__ = 'RoleOther'

    role_id = db.Column(db.Integer, nullable=False, info='角色id')
    other_id = db.Column(db.Integer, info='其他类型的人员id')
    id = db.Column(db.Integer, primary_key=True)



class RoleSchool(db.Model):
    __tablename__ = 'RoleSchool'

    role_id = db.Column(db.Integer, nullable=False, info='角色ID')
    school_id = db.Column(db.Integer, nullable=False, info='院系ID')
    id = db.Column(db.Integer, primary_key=True)



class School(db.Model):
    __tablename__ = 'School'

    id = db.Column(db.Integer, primary_key=True, info='院系id')
    parent_id = db.Column(db.Integer, server_default=db.FetchedValue(), info='父院系id')
    name = db.Column(db.String(30), server_default=db.FetchedValue(), info='院系名称')
    code = db.Column(db.String(30), info='国科大单位代码')
    address = db.Column(db.String(255), info='院系地址')
    other_names = db.Column(db.String(100), info='别名')



class SchoolGroup(db.Model):
    __tablename__ = 'SchoolGroup'

    school_id = db.Column(db.String(20), nullable=False, info='部门ID')
    group_id = db.Column(db.Integer, nullable=False, info='用户组ID')
    id = db.Column(db.Integer, primary_key=True)



class Student(db.Model):
    __tablename__ = 'Student'

    id = db.Column(db.String(20), primary_key=True, info='身份证 护照')
    name = db.Column(db.String(100), info='姓名')
    student_code = db.Column(db.String(20), info='学号')
    phone = db.Column(db.String(20), info='手机号')
    email = db.Column(db.String(50), info='用户邮箱')
    school_id = db.Column(db.Integer, info='所属院系ID')
    first_tutor_job_id = db.Column(db.String(20), info='第一导师工号')
    second_tutor_job_id = db.Column(db.String(20), info='第二导师工号')
    student_type = db.Column(db.String(20), info='学生类型，\r\n1.集中教学\r\n\n2. 校部高年级\r\n\n3. 京区研究所\r\n\n4. 集中教学联培')
    degree = db.Column(db.String(20), info='学生的学位类型，1博士生、2硕士生，3本科生')
    overseas = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否为留学生（1是 0否）')
    start_year = db.Column(db.Integer, info='入学年份')
    class_id = db.Column(db.String(20), server_default=db.FetchedValue(), info='班级编号')
    district_id = db.Column(db.Integer, info='所属校区ID')
    institute_id = db.Column(db.Integer, info='所属研究所ID')
    resident = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否住校（1代表是 0代表否）')
    resident_district_id = db.Column(db.Integer, server_default=db.FetchedValue(), info='住宿的校区id')
    resident_district_address = db.Column(db.String(255), server_default=db.FetchedValue(), info='住宿的详情地址')
    student_status = db.Column(db.String(20), info='学生当前的状态')
    outer_address = db.Column(db.String(100), info='学生在校外的住址')
    intern_address = db.Column(db.String(100), info='学生实习的公司地址')
    is_checked = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否报到（1代表是 0代表否）')
    head_teacher_id = db.Column(db.String(20), info='班主任 老师ID')
    instructor_teacher_id = db.Column(db.String(20), info='辅导员 老师ID')
    institute_teacher_id = db.Column(db.String(20), info='研究所负责老师 老师ID')
    sex = db.Column(db.Integer, info='用户性别（0男 1女 2未知）')
    del_flag = db.Column(db.Integer, server_default=db.FetchedValue(), info='删除标志（0代表存在 1代表删除）')
    avatar = db.Column(db.String(100), info='头像路径')
    remark = db.Column(db.String(500), info='备注')
    unit_code = db.Column(db.String(20), info='单位代码')
    is_not_school = db.Column(db.String(25), info='是否在校')
    management_unit_code = db.Column(db.String(25), info='管理单位code')
    cultivate_unit_name = db.Column(db.String(25), info='培养单位name')
    cultivate_unit_code = db.Column(db.String(25), info='培养单位code')
    management_unit_name = db.Column(db.String(25), info='管理单位name')
    class_name = db.Column(db.String(25), info='班级名称')
    institute_teacher_name = db.Column(db.String(25), info='研究所负责人')
    Institute_accommodation = db.Column(db.String(25), info='住宿研究所')
    campus_accommodation = db.Column(db.String(100), info='住宿校区')
    campus_accommodatio_name = db.Column(db.String(100), info='住宿校区名称')
    resident_school_address = db.Column(db.String(100), info='住宿学校详情')
    resident_institute_address = db.Column(db.String(100), info='住宿研究所详情')



class Teacher(db.Model):
    __tablename__ = 'Teacher'

    id = db.Column(db.String(20), primary_key=True, info='身份证 护照\r\n')
    name = db.Column(db.String(100), nullable=False, info='姓名')
    course_unit = db.Column(db.String(30), info='开课单位')
    unit_name = db.Column(db.String(30))
    teach_unit = db.Column(db.String(30), info='教学单位')
    job_id = db.Column(db.String(30), info='工号')
    dept_id = db.Column(db.Integer, info='所属部门ID，仅为职能部门')
    position = db.Column(db.String(50), info='职位')
    teacher_type = db.Column(db.String(50), info='人员类别，在编、派遣、外包')
    teacher_status = db.Column(db.String(50), info='人员特征，当前所处的状态，境外、病假')
    phone = db.Column(db.String(20), info='手机号')
    email = db.Column(db.String(50), info='用户邮箱')
    sex = db.Column(db.Integer, info='用户性别（0男 1女 2未知）')
    district_id = db.Column(db.Integer, info='所属校区ID')
    school_id = db.Column(db.Integer, info='所属院系ID')
    institute_id = db.Column(db.Integer, info='所属研究所ID')
    resident = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否住宿（1代表是 0代表否）')
    resident_district_id = db.Column(db.Integer, server_default=db.FetchedValue(), info='住宿的校区id')
    active = db.Column(db.Integer, server_default=db.FetchedValue(), info='帐号状态（1正常 0禁用')
    del_flag = db.Column(db.Integer, server_default=db.FetchedValue(), info='删除标志（0代表存在 1代表删除）')
    avatar = db.Column(db.String(100), info='头像路径')
    remark = db.Column(db.String(500), info='备注')
    superior = db.Column(db.String(20))
    is_not_school = db.Column(db.String(25), info='是否在校')
    principal = db.Column(db.String(25), info='直属上级')
    unit_code = db.Column(db.String(25), info='单位code')



class TeacherGroup(db.Model):
    __tablename__ = 'TeacherGroup'

    teacher_id = db.Column(db.String(20), nullable=False, info='老师ID')
    group_id = db.Column(db.Integer, nullable=False, info='用户组ID')
    id = db.Column(db.Integer, primary_key=True)



class TeacherRole(db.Model):
    __tablename__ = 'TeacherRole'

    teacher_id = db.Column(db.String(20), nullable=False, info='老师ID')
    role_id = db.Column(db.Integer, nullable=False, info='角色ID')
    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='插入时间')



class Unit(db.Model):
    __tablename__ = 'Unit'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    code = db.Column(db.String(20))



class WlComment(db.Model):
    __tablename__ = 'wl_Comment'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    comment = db.Column(db.Text)
    insertedAt = db.Column(db.DateTime, server_default=db.FetchedValue())
    ip = db.Column(db.String(100), server_default=db.FetchedValue())
    link = db.Column(db.String(255))
    mail = db.Column(db.String(255))
    nick = db.Column(db.String(255))
    pid = db.Column(db.Integer)
    rid = db.Column(db.Integer)
    sticky = db.Column(db.Integer)
    status = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue())
    like = db.Column(db.Integer)
    ua = db.Column(db.Text)
    url = db.Column(db.String(255))
    createdAt = db.Column(db.DateTime, server_default=db.FetchedValue())
    updatedAt = db.Column(db.DateTime, server_default=db.FetchedValue())



class WlCounter(db.Model):
    __tablename__ = 'wl_Counter'

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Integer)
    reaction0 = db.Column(db.Integer)
    reaction1 = db.Column(db.Integer)
    reaction2 = db.Column(db.Integer)
    reaction3 = db.Column(db.Integer)
    reaction4 = db.Column(db.Integer)
    reaction5 = db.Column(db.Integer)
    reaction6 = db.Column(db.Integer)
    reaction7 = db.Column(db.Integer)
    reaction8 = db.Column(db.Integer)
    url = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    createdAt = db.Column(db.DateTime, server_default=db.FetchedValue())
    updatedAt = db.Column(db.DateTime, server_default=db.FetchedValue())



class WlUser(db.Model):
    __tablename__ = 'wl_Users'

    id = db.Column(db.Integer, primary_key=True)
    display_name = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    email = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    password = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    type = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue())
    label = db.Column(db.String(255))
    url = db.Column(db.String(255))
    avatar = db.Column(db.String(255))
    github = db.Column(db.String(255))
    twitter = db.Column(db.String(255))
    facebook = db.Column(db.String(255))
    google = db.Column(db.String(255))
    weibo = db.Column(db.String(255))
    qq = db.Column(db.String(255))
    _2fa = db.Column('2fa', db.String(32))
    createdAt = db.Column(db.DateTime, server_default=db.FetchedValue())
    updatedAt = db.Column(db.DateTime, server_default=db.FetchedValue())
