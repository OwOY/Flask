# Flask


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
