# hema-dingdong-yunli-zhushou
# 环境：
## python 3.0 
## node.js 稳定版

该工具是通过post方式监控叮咚的运力以及用get方式监控盒马的运力。
该脚本已经解决叮咚snars生成问题。

# 盒马：
只需要在手机端打开商品页，建议挑选一个一直有货的商品推荐贵的酒类可以长期监控。

# 叮咚：
## 4月23日已更新
1. 需要抓包，手机或者电脑登录叮咚小程序。
2. 打开小程序中我的，然后需要通过抓包获取 https://trackercollect.ddxq.mobi/appInfo/bundle 中的request信息。
3. 通过网页解码encodeURIComponent http://tools.jb51.net/transcoding/urlencode_decode
4. 按抓包填入header以及data
