const form=document.getElementById("form");
form.addEventListener("submit",async e=>{
 e.preventDefault();
 const msg=document.getElementById("msg");
 try{
  if(location.pathname.includes("register")){
   await api("/auth/register",{method:"POST",body:JSON.stringify({name:name.value,email:email.value,password:password.value})});
   msg.innerHTML='<div class="alert alert-success">Registered. You can now login.</div>';
  }else{
   const data=await api("/auth/login",{method:"POST",body:JSON.stringify({email:email.value,password:password.value})});
   localStorage.setItem("jobtrack_token",data.access_token);
   location.href="/dashboard.html";
  }
 }catch(err){msg.innerHTML=`<div class="alert alert-danger">${err.message}</div>`;}
});