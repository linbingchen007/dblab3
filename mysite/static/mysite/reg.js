
function check(){
	if (document.getElementById("password_confirm").value == "") {
		alert("密码不可以为空");
	}else{
	if (document.getElementById("password_confirm").value == document.getElementById("password").value){
		document.getElementById("submitform").action="/mv/handlereg"
		document.getElementById("submitform").submit();
	}else{
		alert("二次密码输入不一致");
	}
}
}