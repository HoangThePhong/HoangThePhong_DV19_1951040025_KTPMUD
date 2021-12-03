select *
from salesman s, 
(select city, MAX(commission) max_commission from salesman
group by city) rs
where s.city = rs.city and s.commission = rs.max_commission

