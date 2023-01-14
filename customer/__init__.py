s = """\n##0223add for调用 km es 数据，根据数据库的目录区分 - 指标服务特有\nelasticsearch-kmuri: prod.es.shangjian.tech\nelasticsearch-kmusername: shangjian\nelasticsearch-kmpassword: nginx_pass\n\n\n#标识用，启动的时候可以看日志来确认跑的配置文件的正确性\nspring-profiles-active: test\n\n#airworks
    地址\nairworks-addr: http://10.40.35.142:30000\nairworks-token: gAAAAABhLufXTWtW6a28Im_myfHKgGBghgdWWpAfWgvQTLgwiHQOmcuQEWHMId7AIlf9NN0MzEM8EFfa_h5YII1PsnnQP_MAjQ==\n\n#缩略图服务 todo 问下怎么部署（之前说是前端的一个无头服务器的功能）\nstatic-endpoint-url: 10.121.2.193\nstatic-endpoint-port: 31860\n\n#xxl-job 服务端地址，若集群用逗号隔开\nxxl-job-admin-addresses: http://172.28.8.10:30094/xxljobadmin\n\n\n\n\n#
    \npkslow:\n  age: 999\n\n#mysql相关配置\nmysql-url: 172.28.56.86:4000\nmysql-dbname: km_backend_init\nmysql-username: km_java\nmysql-password: KM@java123\n\n#redis配置\nredis-host: 172.28.56.113\nredis-port: 6379\nredis-password: Shangjian@123\n\n#eagle网关\neagle-localhost: 172.28.8.17:30093\n\n#elasticsearch
    elasticsearch-password:\n#只有一个es的情况，下面两个es 填写成一样的即可，第一个是业务es地址，第二个是 系统指标所在的地址\nelasticsearch-uri: 172.28.8.15\nelasticsearch-sysuri: dev.es.shangjian.tech\nelasticsearch-port: 9200\nelasticsearch-tport: 9300\nelasticsearch-username:\nelasticsearch-cluserName: shangjian-guangfa-es-5.5.3\n\n#股票跟踪库模板解析服务- docker.valuesimplex.com/common/template_parse_server:latest
    parse-template-endpoint: 172.28.8.17:30087\n\n# 前端网址\nfrontend-url: http://172.28.8.30:30097\n# minio上传的文件服务器地址\nminio-url: http://172.28.8.77:32265\n\n#Kmp项目通用参数\n#
    kmp-super_institution: 熵简科技\nquery.third_party_query: true\nspring.application.name: kmp-indicator\n\nparse:\n
    indicator:\n    url: http://172.28.8.17:30087/temp/indicator/parse/\n    \n#nacos 注册中心配置\nspring-cloud-nacos-discovery-server-addr: 172.28.56.113:8848,172.28.56.40:8848,172.28.56.121:8848\nspring-cloud-nacos-discovery-namespace: 5905277e-bb49-482d-a992-40a701fb753c\nspring-cloud-nacos-discovery-group: KMP_DEV\n\nspring:\n
    profiles:\n    active: test\n# 到2999年过期的\nlicense: 'c2hhbmdqaWFuLmV4cGlyZT0yOTk5LTAxLTAxY2Q4ODEyYzUyYjk1N2MxNjlmNzA3MjE4OGNlZmQ1ZTkwNTcyNzdjZDFjYmNiYjVhNmNlODYyNTE3MTA4Yjk4ZmU4NmE0YWI3MGQ5MWJhNDI5YzUzY2Y0OGE5ZDA4YTkzYzA1Y2FmNjI2OWUyN2ZhMDExYTkzNTFiYjNlNjgwZDY2MWI1MmMzYWQ5YTgwMDhlNDMyZjEyN2Q1OGI5MzAwYjJjNmU3YjViNGRhZGY2OGEyYmUyZjgxODgzZTIwM2RkOTgyYWJmMmU3ODUxZjhiOTI0Njg1ZjQ3Nzc0NzI5N2E1MTJiZjRmMzYwYzA5YjA4YTY0NDg4YmJmM2NkYWFjZQ=='\n"""

# print(s)

import time

start = time.time()

for i in range(250000000):
    a = i

end = time.time()
print(end - start)
