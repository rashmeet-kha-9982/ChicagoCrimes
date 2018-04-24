%sql
select district, count(1) value
from crime
group by district 
order by district

%sql 
select arrest, count(1) value 
from crime 
where primaryType="${primaryType=THEFT,THEFT|BATTERY|CRIMINAL DAMAGE}" 
group by arrest 
order by arrest

%sql 
select primaryType, count(1) value
from crime 
group by primaryType
order by primaryType

