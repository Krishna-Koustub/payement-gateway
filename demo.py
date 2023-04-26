keyid ='rzp_test_FUqs0pZN90i6wG'
keySecret = '9rJnCrTODkBlSPCUs0ioCzN1'

import razorpay

client = razorpay.Client(auth=(keyid, keySecret))

data = {
    'amount' : 100*100,
    "currency": "INR",
    "receipt" : "krishnakoustub",
    "notes" :
    {
        "name" : "krishna",
        "payment_for" : "Angular course"
    }
}

#server orderid 
order = client.order.create(data=data)
print(order)



# {'id': 'order_Jy3Qu7hNihLgMa', 'entity': 'order', 'amount': 10000, 'amount_paid': 0, 'amount_due': 10000, 'currency': 'INR', 'receipt': 'krishnakoustub', 'offe

#r_id': None, 'status': 'created', 'attempts': 0, 'notes': {'name': 'krishna', 'payment_for': 'Angular course'}, 'created_at': 1658851543}