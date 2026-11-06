const field=document.getElementById('search'),results=document.getElementById('results'),status=document.getElementById('search-status');
const root=document.body.dataset.root;
let indexPromise;
async function search(){
 const query=field.value.trim().toLowerCase();results.replaceChildren();
 if(!query){status.textContent='';return;}
 status.textContent='正在搜索…';
 try{
  indexPromise??=fetch(root+'search.json').then(r=>{if(!r.ok)throw Error('Search unavailable');return r.json();});
  const index=await indexPromise;if(field.value.trim().toLowerCase()!==query)return;
  const terms=query.split(/\s+/);const matches=index.map(p=>({...p,score:terms.every(t=>(p.title+' '+p.text).toLowerCase().includes(t))?1+terms.filter(t=>p.title.toLowerCase().includes(t)).length*10:0})).filter(p=>p.score).sort((a,b)=>b.score-a.score);
  status.textContent=`${matches.length} 个结果${matches.length>30?' · 显示前 30 项':''}`;
  for(const page of matches.slice(0,30)){const a=document.createElement('a');a.href=root+page.url;a.textContent=page.title;results.append(a);}
 }catch{indexPromise=undefined;status.textContent='搜索暂不可用，请使用全部文档目录。';}
}
let timer;field.addEventListener('input',()=>{clearTimeout(timer);timer=setTimeout(search,180);});
