# insert data such as in donation
INSERT INTO donation(don_id,
                     given_charity, given_zakat, tnx_number)
VALUES(1234, 1200, 1200, 'new')

# update data such as representative relation
UPDATE representative
SET address = 'raozan'
WHERE user_name = 'cuet_med'

# show total amount
SELECT sum(given_charity) as charity,
sum(given_zakat) as zakat
FROM donation


# show the amount received by an rep
SELECT sum(recv_charity), sum(recv_zakat)
FROM representative
JOIN received_amount
ON representative.company_id = received_amount.rep_id
WHERE company_name = "rep_id"


# admin creats a transaction to rep such as zakat
# we can search first lowest amount and update it
SELECT tranx_id, given_zakat
FROM donation
WHERE given_zakat > 0
ORDER BY given_zakat asc
LIMIT 1
UPDATE donor_list SET zakat = given_zakat
WHERE rcv_tid = 123 AND don_tid = tranx_id
