import argparse
import os
from os.path import join
from pathlib import Path

import toolits
if __name__ == '__main__':
    argp = argparse.ArgumentParser()

    argp.add_argument("model", help="<UNK>")
    argp.add_argument("-u", "--url",required=True,help="api url")
    argp.add_argument("-k", "--apikey", required=True, help="api key")
    argp.add_argument("-i", "--input", required=True, help="input file or dir")
    argp.add_argument("-r", "--read-dir")
    argp.add_argument("-p", "--base-path")
    argp.add_argument("--tags",nargs="+",type=str, help="tags")
    args = argp.parse_args()

    if args.k not in "Bearer":
        args.k = f"Bearer {args.k}"
    toolits.url = args.url
    toolits.apikey = args.k

    pl = toolits.page_list()
    if args.model == "getlist":

            ll = toolits.get_dir_tree(pl)
            print(ll)
    elif args.model == "download":
            print("downloading")
            print("page_num:",len(pl))
            toolits.download_all_pages(pl,args.d)
    elif args.model == "upload":
            if args.r:
                for root,dirs,files  in os.walk(args.i):
                    for i in files:
                        title = i.replace(".md","")
                        uppath = args.base_path+root.replace(args.i,"")+title
                        file = open(join(root,i), "r").read()
                        toolits.upload_wiki(file, title, args.tags, path=uppath)
            else:
                file = open(args.i,"r").read()
                pth =Path(args.i)
                toolits.upload_wiki(file,pth.stem,args.tags,path=args.base_path)







    ...
