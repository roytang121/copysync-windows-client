CopySync Windows Client
==============================
A sample client side application that monitor the clipboard data changes and commit changes to copysync-server on every copy intent (Ctrl + C and any other ways of copying)

##Installation
running from console
```cmd
python main.py
```

##Usage
You may start a local server or use the remote server as shown in the sample application.
The POST request takes only one parameter :
```json
{
	'data': your_clipboard_text,
}
```
