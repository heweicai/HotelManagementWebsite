//$(document).ready(function(){
//    alert("欢迎登录温馨堂");
//    $("#login").click(function(){
//        var user = $("#username").val();
//        var pwd = $("#password").val();
//        alert("当前用户为: "+user);
//    });
//});
function getCookie(name){
    var x = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return x ? x[1]:undefined;
}

$(document).ready(function(){
    //alert("欢迎登录温馨堂");
    $("#login").click(function(){
        var user = $("#username").val();
        var pwd = $("#password").val();
        var pd = {"username":user, "password":pwd, "_xsrf":getCookie("_xsrf")};
        $.ajax({
            type:"post",
            url:"/",
            data:pd,
            cache:false,
            success:function(data){
              alert(data);
              window.location.href = "/sysmanagement/home?home="+data;   //登入成功后跳转页面
            },
            error:function(){
                alert("连接异常!");
                window.location.href = "/error";
            },
        });
    });
});