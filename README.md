# hema-dingdong-yunli-zhushou
环境：
python 3.0 
node.js 稳定版

该工具是通过post方式监控叮咚的运力以及用get方式监控盒马的运力。
该脚本已经解决叮咚snars生成问题。

盒马：
只需要在手机端打开商品页，建议挑选一个一直有货的商品推荐贵的酒类可以长期监控。

叮咚：
需要抓包，手机或者电脑登录叮咚小程序，然后添加商品到购物车并进行下单操作，不需要提交订单，然后将以下两个链接中的hearder和data填写到对应栏目即可。

https://maicai.api.ddxq.mobi/order/getMultiReserveTime
https://maicai.api.ddxq.mobi/cart/index
