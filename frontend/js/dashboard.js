if(!token()) location.href="/login.html";
document.getElementById("logout").onclick=()=>{localStorage.removeItem("jobtrack_token");location.href="/";};
(async()=>{
 try{
  const d=await api("/dashboard/stats");
  document.getElementById("cards").innerHTML=[
   ["Applications",d.total_applications],["Interviews",d.interviews],["Offers",d.offers],["Rejected",d.rejected]
  ].map(x=>`<div class="col-6 col-lg-3"><div class="card shadow-sm"><div class="card-body"><small class="text-muted">${x[0]}</small><h2>${x[1]}</h2></div></div></div>`).join("");
  document.getElementById("stats").textContent=JSON.stringify(d.by_status,null,2);
 }catch(e){document.getElementById("stats").textContent=e.message;}
})();