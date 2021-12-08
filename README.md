# Flask

### Request
- 取得json  
```
request.get_json()
```
- 取得Form Data  
```
request.get_form()
```
- 取得headers  
```
request.headers
```
- 取得參數  
```
request.args.get
```
- 取得Route
```
request.path
```
### Route變數  
```
@api.route('/<page>')
def view(page):
    print(f'現在是第{page}頁')
    return 'OK'
```
### 上傳物件  
```
@api.route('/')
def upload():
    return send_from_directory('{path}', '{file}', as_attachment=True)   #as_attachment決定要顯示在頁面或是直接下載 
```
