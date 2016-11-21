# coding:utf-8

IMAGE_CODE_VALIDITY = 120   # 图片验证码有效期 秒
SMS_CODE_VALIDITY = 300   # 短信验证码有效期 秒

HOME_PAGE_MAX_HOUSES = 5 # 主页房屋展示最大数量
HOME_PAGE_DATA_REDIS_EXPIRE_SECOND = 7200 # 主页缓存数据过期时间 秒

AREA_INFO_REDIS_EXPIRE_SECOND = 7200 # 城区信息缓存时间 秒

HOUSE_LIST_PAGE_CAPACITY = 3 # 房屋列表页每页数目
HOUSE_LIST_REIDS_CACHED_PAGE = 2 # redis每次缓存房屋列表页数
HOUSE_LIST_REDIS_EXPIRE_SECOND = 3600 # 房屋列表缓存时间 秒
HOUSE_DETAIL_REDIS_EXPIRE_SECOND = 7200 # 房屋详情缓存时间 秒

HOUSE_DETAIL_COMMENT_DISPLAY_COUNTS = 30 # 房屋详情页评论显示个数