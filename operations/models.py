from django.db import models

# Create your models here.

OPS_STATUS = (
    (str(1), u"使用中"),
    (str(2), u"未使用"),
    (str(3), u"故障"),
    (str(4), u"其它"),
)

OPS_LEVER = (
    (str(1), u"1"),
    (str(2), u"2"),
)

DEPARTMENT = (
    ("yyglb", "运营管理部"),
    ("hlwjrb", "互联网金融部"),
    ("xxkfb", "信息开发部"),
    ("ersyb", "E融事业部"),
    ("yhkb", "银行卡部"),
    ("gjyw", "国际业务部"),
)

class OpsServer(models.Model):
    name = models.CharField("系统名称(简)", max_length=20)
    full_name = models.CharField("系统名称(全)", max_length=20)
    number = models.CharField("系统编号",max_length=10)
    lever = models.CharField("系统层级",choices=(('1','1'),('2','2')),max_length=20)
    en_name = models.CharField("英文缩写", max_length=20,null=True)
    platform = models.CharField("所属平台", max_length=20,null=True)
    old_lever = models.CharField("系统级别(旧)",max_length=20,null=True)
    new_lever = models.CharField("重要级别",max_length=20,null=True)
    department = models.CharField("所属部门",choices=DEPARTMENT,max_length=20,null=True)
    status = models.CharField("系统状态", choices=OPS_STATUS, max_length=20)
    ha_ip = models.GenericIPAddressField("HA地址", max_length=50,null=True)
    manager = models.CharField("运营负责人", max_length=50, null=True)
    dev_manager = models.CharField("开发负责人", max_length=50, null=True)
    sale_manager = models.CharField("业务负责人", max_length=50, null=True)
    vendor = models.CharField("开发商", max_length=50, null=True)
    vendor_person = models.CharField("开发商联系人", max_length=50, null=True)
    vendor_phone = models.CharField("开发商联系电话", max_length=50, null=True)
    online_time = models.DateTimeField("投产时间",null=True,blank=True)
    create_time = models.DateTimeField("创建时间", auto_now_add=True, null=True)
    mobity_time = models.DateTimeField("修改时间", auto_now=True, null=True)
    def __str__(self):
        return self.name

class OpsHost(models.Model):
    hostname = models.CharField("主机名", max_length=50, null=True, blank=True)
    ip = models.GenericIPAddressField("主机IP", max_length=15)
    system = models.CharField("主机系统", max_length=50, null=True, blank=True)
    manager = models.CharField("主机管理人员", max_length=50, null=True)
    use_port1 = models.CharField("使用的端口", max_length=50, null=True)
    use_port2 = models.CharField("使用的端口", max_length=50, null=True)
    use_port3 = models.CharField("使用的端口", max_length=50, null=True)
    use_port4 = models.CharField("使用的端口", max_length=50, null=True)
    status = models.CharField("使用状态", choices=OPS_STATUS ,max_length=20, null=True, blank=True)
    ops_server = models.ForeignKey('OpsServer', on_delete=models.CASCADE)
    create_time = models.DateTimeField("创建时间", auto_now_add=True, null=True)
    mobity_time = models.DateTimeField("修改时间", auto_now=True, null=True)

    def __str__(self):
        return self.hostname
