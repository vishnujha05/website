const list_name = ['vishnu', 'jha','yaakov sir','jason','paul','jim','payal','simran','rahul', 'mishra', 'John'];
console.log(list_name)
for(var i=0;i,list_name.length;i++){
    if(list_name[i][0]=='j'||list_name[i][0]=='J'){
    console.log('good bye ' + list_name[i]);
    }
    else{
    console.log('Hello ' + list_name[i]);
    }
}