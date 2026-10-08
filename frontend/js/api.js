const API = "/api";
function token(){return localStorage.getItem("jobtrack_token");}
async function api(path, options={}) {
  const headers = {"Content-Type":"application/json", ...(options.headers||{})};
  if(token()) headers.Authorization = `Bearer ${token()}`;
  const res = await fetch(API+path, {...options, headers});
  const data = await res.json().catch(()=>null);
  if(!res.ok) throw new Error(data?.detail || "Request failed");
  return data;
}
