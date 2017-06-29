import tensorflow as tf

x1 = tf.constant(5) # Just values not even array's (single scalar)
x2 = tf.constant(6)

# Inefficient way to do this is:
# result = x1*x2

# Much more efficient way to do this:
result = tf.multiply(x1, x2) # Use matmul instead of multiply when value inside constant is array
# Also when using matmul, you need to specify shape of the tensor(matrix) and they should comply with m*n `into` n*m rule 
# result = x1*x2 also gives tensor element after multiplication

print result # Gives: Tensor("Mul:0", shape=(), dtype=int32) just an abstract tensor in our computational graph

# To see the actual result we use session (what I think is this way tensorflow is much more close to C++ programming nature, correct me if I am wrong)
# sess = tf.Session()
# print sess.run(result) # This will give the actual result, basically start's the session and run's the graph so no computation  happened until to used run session method
# sess.close()

# or what we can do and should do is:
# Remember we can save tensorflow seeion output to python variable itself, it's like graph running backward and giving us the output
with tf.Session() as sess:
 	print sess.run(result) ## This will automatically close the session at the end