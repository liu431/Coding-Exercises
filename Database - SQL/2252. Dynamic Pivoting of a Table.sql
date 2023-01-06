CREATE PROCEDURE PivotProducts()
BEGIN
	# Write your MySQL query statement below.
    set session group_concat_max_len = 1000000; # default is 1024
    
	set @query = null;
	select group_concat(
		distinct concat(
			'sum(if(store = "', store, '", price, null)) as ', store
		)
	)
	into @query
	from Products;

	set @query = concat('select product_id, ', @query, ' from Products group by 1');

	prepare stmt from @query;
	execute stmt;
	deallocate prepare stmt;

END
