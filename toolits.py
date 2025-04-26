import os
import pathlib
from pathlib import Path
import requests
import graphql_query
from graphql_query import Operation, Query, Argument
apikey="Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcGkiOjMsImdycCI6MSwiaWF0IjoxNzQ1MzMyMjA1LCJleHAiOjE4NDAwMDUwMDUsImF1ZCI6InVybjp3aWtpLmpzIiwiaXNzIjoidXJuOndpa2kuanMifQ.KN6hsgaM_pxBHGF2wc7dcPyvXIxO2zx6hSFu7HjYwz0BZpaBE09Re4brgCYWWbx5oHT1hox7fVX-vXWOIZg-eiH5QE8HV1bDGOUYweUA_5U_1XOVIPWLYseAgJ-5X_sU1uhKCtHivCWMAvR3wPway_J22zVy5N0TTk6oR5SjuKcNJ6djNfPt2my1VFBVxLFqkmsrrsEnEfv-7J7EZfo5CO7lRkBnyU5ROuKCCuE10cQc5RDddIEgik_RcRUiFeqcETTjV6Kfoa_Zz7D9HlJQXj-4WpQkqGvRwSQr7AUfuEtW6p2VBzTVSawj3Ubd6EP0TXipZu9rnxx_rmbxhjzXZg"
url = "http://192.168.1.9:3010/graphql"
def upload_wiki(content,title,tags:list[str],path="",description=""):

    fds=[Argument(name="content",value=""),
Argument(name="description",value=""),
Argument(name="isPublished",value="true"),
Argument(name="isPrivate",value="false"),
Argument(name="locale",value="zh"),
Argument(name="path",value=""),
Argument(name="tags",value=[]),
Argument(name="title",value=""),
Argument(name="editor",value="markdown"),
]




    create= Query(name="create",arguments=fds,fields=[" id",
                "path",
                "hash",
                "title"] )
    aaee = Operation(type="pages",queries=[create])
    query(aaee.render())

def query(data):
    aa = requests.post(url,json={"query":"{"+data+"}"},headers={"Authorization":apikey})

    return aa.json()
def page_list():
    list_query = Query(name="list", fields=[
        "path",
       'id',
        "tags",
        "locale",
        "title"
    ])

    aaee = Operation(type="pages", queries=[list_query])

    return  query(aaee.render())

def get_page_context(id):
    fds = [
        Argument(name="id", value=id)
    ]


    single_query = Query(
        name="single",
        arguments=fds,
        fields=[
            "content",
            "editor"
        ]
    )


    aaee = Operation(
        type="pages",
        queries=[single_query]
    )
    return query(aaee.render())

def list_astess(id):
    fds = [
        Argument(name="folderId", value=id),
        Argument(name="kind", value="ALL")  # Adjust type if needed
    ]

    # Create the list query with fields
    list_query = Query(
        name="list",
        arguments=fds,
        fields=[
            "id",
            "filename",
            "ext",
            "kind",
            "mime",
            "fileSize",
            "metadata",
            "createdAt",
            "updatedAt"
        ]
    )


    aaee = Operation(
        type="assets",  # Optional - name your query
        queries=[list_query]
    )
    return query(aaee.render())

def download_all_pages(pl,basedir="./wiki"):


    for i in pl['data']["pages"]["list"]:
        data = get_page_context(i['id']) ['data']['pages']['single'] # ckeditor #markdown
        docdir = Path(basedir,i['path'])
        os.makedirs(docdir.parent,exist_ok=True)
        if data['editor']=="markdown":
            open(str(docdir)+".md","w",encoding="utf-8").write(data["content"])
        elif data['editor']=="ckeditor":
            open(str(docdir) + f".html", "w", encoding="utf-8").write(data["content"])
        print("download:", i['path'])
def get_dir_tree(pl):
    tree =[]

    for i in pl['data']["pages"]["list"]:
        tree.append(i["path"])
    return tree
def paths_to_dict(paths):
            result = {}
            for path in paths:
                parts = path.strip('/').split('/')  # 去掉首尾的/并按/分割
                if len(parts) != 3:  # 确保是三层路径
                    continue

                # 获取各级路径部分
                first, second, third = parts

                # 如果第一级键不存在，创建并初始化为空字典
                if first not in result:
                    result[first] = {}

                # 设置第二级键值对
                result[first][second] = third

            return result