# WikiJS  Tool

## 简介
这是一个用于与 WikiJS API 交互的工具，支持获取页面列表、下载页面以及上传 Markdown 文件到 WikiJS 的功能。

---

## 功能
1. **获取页面列表**：从 WikiJS 获取所有页面的列表。
2. **下载页面**：将 WikiJS 中的所有页面下载到本地。(暂时不支持图片)
3. **上传页面**：将本地的 Markdown 文件上传到 WikiJS。(暂时不支持图片)

---

## 使用方法

### 安装依赖
确保已安装 Python 环境，并安装以下依赖：
pip install -r requirements.txt
---

### 参数说明
执行脚本时需要提供以下参数：

| 参数       | 类型   | 是否必填 | 描述                                                                                   |
|------------|--------|----------|--------------------------------------------------------------------------------------|
| `model`    | string | 是       | 操作模式，可选值：`getlist`（获取页面列表）、`download`（下载页面）、`upload`（上传页面） |
| `-u, --url`| string | 是       | WikiJS API 的 URL                                                                    |
| `-k, --apikey` | string | 是       | WikiJS API 的密钥                                                                   |
| `-i, --input` | string | 是       | 输入文件或目录路径                                                                  |
| `-r, --read-dir` | string | 否       | 是否递归读取目录，默认为否                                                         |
| `-p, --base-path` | string | 否       | 基础路径，用于上传时指定页面路径                                                   |
| `--tags`   | list   | 否       | 页面标签，多个标签用空格分隔                                                        |

---

### 示例

#### 1. 获取页面列表
`python main.py getlist -u https://example.com/api/v2 -k your_api_key`
#### 2. 下载所有页面
`python main.py download -u https://example.com/api/v2 -k your_api_key -i output_dir`
#### 3. 上传单个 Markdown 文件
`python main.py upload -u https://example.com/api/v2 -k your_api_key -i file.md --tags tag1 tag2 -p /path/in/wiki`
#### 4. 上传整个目录中的 Markdown 文件

`python main.py upload -u https://example.com/api/v2 -k your_api_key -i input_dir --read-dir -p /path/in/wiki --tags tag1 tag2`
---

## 注意事项
1. **API Key 格式**：如果提供的 API Key 不以 `Bearer` 开头，程序会自动添加前缀。
2. **输入路径**：确保提供的输入路径正确且存在。
3. **权限**：确保 API Key 具有相应的权限以执行相关操作。

---

## 贡献
欢迎提交 Issue 或 Pull Request 来改进此工具！

---