# -*- coding: utf-8 -*-
# This file is to be used with py.test

import sys
sys.path = ['.'] + sys.path #adding current working directory to the $PYTHONPATH
import numpy
import numpy.linalg
import numpy.random
from numpy.testing import assert_almost_equal, assert_array_almost_equal, assert_array_equal, assert_equal
from adolc import *

def test_constructors():
	a = adouble(13.);
	b = adouble(5)
	c = adouble(a)
	
	assert a.val == 13.
	assert b.val == 5
	assert c.val == 13.
	
def test_unary_operators():
	a = adouble(1.)
	b = -a
	assert b.val == -1.
	assert a.val == 1.
	
	print type(b)
	print type(a)

def test_conditional_operators():
	ax = adouble(2.)
	ay = adouble(1.)

	assert ax <= 2
	assert ax <= 2.
	assert not ax < 2
	assert not ax < 2.
	

	assert ax >= 2
	assert ax >= 2.
	assert not ax > 2
	assert not ax > 2.

	assert ax >  ay
	assert ax >= ay
	assert not ax <  ay
	assert not ax <= ay
	
	
def test_radd():
	a = adouble(1.)
	b = a + 2.
	c = a + 2.
	d = 2.+ a
	
	assert a.val == 1.

def test_add():
	a = adouble(1.)
	b = a + 2.
	c = a + 2
	d = 2.+ a
	e = 2 + a
	
	assert b.val == 3.
	assert c.val == 3.
	assert d.val == 3.
	assert e.val == 3.
	
def test_sub():
	a = adouble(1.)
	b = a - 2.
	c = 2.- a
	
	assert b.val == -1.
	assert c.val == 1.
	
def test_mul():
	a = adouble(1.5)
	b = a * 2.
	c = 2.* a
	
	assert b.val == 3.
	assert c.val == 3.
	
def test_div():
	a = adouble(3.)
	b = a/2.
	c = 2./a
	
	assert b.val == 3./2.
	assert c.val == 2./3.
	
def test_pow():
	r  = 5
	x = 3.
	y = 2.
	ax = adouble(x)
	ay = adouble(y)
	
	az1 = ax**ay
	az2 = ax**r
	az3 = r**ax
	
	assert_almost_equal(az1.val, x**y)
	assert_almost_equal(az2.val, x**r)
	assert_almost_equal(az3.val, r**x)
	
def test_hyperbolic_functions():
	x = 3.
	ax = adouble(x)
	
	ash = numpy.sinh(ax)
	ach = numpy.cosh(ax)
	ath = numpy.tanh(ax)
	
	assert_almost_equal(ash.val, numpy.sinh(x))
	assert_almost_equal(ach.val, numpy.cosh(x))
	assert_almost_equal(ath.val, numpy.tanh(x))
	
#def test_arc_hyperbolic_functions():
	#x = 3.
	#ax = adouble(x)
	
	#aarcsh = numpy.arcsinh(ax)
	#aarcch = numpy.arccosh(ax)
	#aarcth = numpy.arctanh(ax)
	
	#assert_almost_equal(aarcsh.val, numpy.arcsinh(x))
	#assert_almost_equal(aarcch.val, numpy.arccosh(x))
	#assert_almost_equal(aarcth.val, numpy.arctanh(x))

def test_abs():
	x = 3.
	xs = numpy.array([1.,2.,3.])
	ax = adouble(x)
	axs = adouble(xs)
	
	afabs = numpy.fabs(ax)
	afabss = numpy.fabs(axs)
	
	
	assert_almost_equal(afabs.val, numpy.fabs(x))
	
	#test_expression('fabs (a)     : ',		lambda x: numpy.fabs (x),  a,		a.val)



def test_independent():
	# 0D
	ax = adouble(1)
	bx = independent(ax)
	assert ax == bx
	
	# 1D
	N = 10
	ax = numpy.array([adouble(n) for n in range(N)])
	bx = independent(ax)
	assert numpy.prod( ax == bx )
	
	# 2D
	N = 2; M=3
	ax = numpy.array([[adouble(n+m) for n in range(N)] for m in range(M)])
	bx = independent(ax)
	assert numpy.prod( ax == bx )
	
def test_dependent():
	# 0D
	ax = adouble(1)
	bx = dependent(ax)
	assert ax == bx
	
	# 1D
	N = 10
	ax = numpy.array([adouble(n) for n in range(N)])
	bx = dependent(ax)
	assert numpy.prod( ax == bx )
	
	# 2D
	N = 2; M=3
	ax = numpy.array([[adouble(n+m) for n in range(N)] for m in range(M)])
	bx = dependent(ax)
	assert numpy.prod( ax == bx )
	


def test_hov_ti_reverse():
	"""compute the first columnt of the hessian of f = x_1 x_2 x_3"""
	def f(x):
		return x[0]*x[1]*x[2]
	
	#tape f
	ax = numpy.array([adouble(0.) for i in range(3)])
	trace_on(0)
	for i in range(3):
		independent(ax[i])
	ay = f(ax)
	dependent(ay)
	trace_off()

	x = numpy.array([3.,5.,7.])
	V = numpy.zeros((3,1))
	V[0,0]=1

	(y,W) = hos_forward(0,x,V,2)
	assert y[0] == 105.
	assert W[0] == 35.

	U = numpy.zeros((1,1,2), dtype=float)
	U[0,0,0] = 1.

	Z = hov_ti_reverse(0,U)[0]
	print Z[0,:,0]
	assert numpy.prod( Z[0,:,0] == numpy.array([35., 21., 15.]))
	assert numpy.prod( Z[0,:,1] == numpy.array([0., 7., 5.]))

def test_simple_function():
	def f(x):
		y1 = 1./(numpy.fabs(x))
		y2 = x*5.
		y3 = y1 + y2
		return y3
	def g(x):
		return -1./numpy.fabs(x)**2 + 5.

	#tape f
	trace_on(0)
	x = 2.
	ax = adouble(x)
	independent(ax)
	ay = f(ax)
	depends_on(ay)
	trace_off()
	assert_array_almost_equal(g(x), gradient(0,numpy.array([x])))

def test_tape_to_latex():
	N = 40
	def scalar_f(x):
		return 0.5*numpy.dot(x,x)

	x = numpy.array([1.*n for n in range(N)])
	ax = adouble(x)
	
	trace_on(123)
	independent(ax)
	ay = scalar_f(ax)
	dependent(ay)
	trace_off()
	y = numpy.zeros(1)
	tape_to_latex(123,x,y)
	import os
	os.system("mv tape_123.tex /tmp")
	cwd = os.getcwd()
	os.chdir("/tmp")
	os.system("pdflatex tape_123.tex ")
	os.chdir(cwd)



#######################################################################
## TESTING HIGH LEVEL CONVENICENCE FUNCTIONS (GRADIENT,HESSIAN, ETC..)
#######################################################################

def test_function():
	N = 10
	def scalar_f(x):
		return numpy.dot(x,x)

	x = numpy.ones(N)
	ax = adouble(x)
	
	trace_on(0)
	independent(ax)
	ay = scalar_f(ax)
	dependent(ay)
	trace_off()
	assert_almost_equal(scalar_f(x),function(0,x))
	
def test_gradient():
	N = 10
	def scalar_f(x):
		return 0.5*numpy.dot(x,x)

	x = numpy.array([1.*n for n in range(N)])
	ax = adouble(x)
	
	trace_on(0)
	independent(ax)
	ay = scalar_f(ax)
	dependent(ay)
	trace_off()
	assert_array_almost_equal(x,gradient(0,x))
	
def test_hessian():
	N = 10
	def scalar_f(x):
		return 0.5*numpy.dot(x,x)

	x = numpy.array([1.*n for n in range(N)])
	ax = adouble(x)
	
	trace_on(0)
	independent(ax)
	ay = scalar_f(ax)
	dependent(ay)
	trace_off()
	true_H = numpy.eye(N)
	assert_array_almost_equal(true_H, hessian(0,x))

def test_jacobian():
	N = 31 # dimension
	M = 29 # codimension
	A = numpy.array([[ 1./N +(n==m) for n in range(N)] for m in range(M)])
	def vector_f(x):
		return numpy.dot(A,x)
		
	x = numpy.array([1.*n for n in range(N)])
	ax = adouble(x)
	
	trace_on(123)
	independent(ax)
	ay = vector_f(ax)
	dependent(ay)
	trace_off()
	assert_array_almost_equal(A, jacobian(123,x))
	
def test_hess_vec():
	N = 1132
	def scalar_f(x):
		return 0.5*numpy.dot(x,x)

	x = numpy.array([1.*n for n in range(N)])
	ax = adouble(x)
	
	trace_on(0)
	independent(ax)
	ay = scalar_f(ax)
	dependent(ay)
	trace_off()
	
	v = numpy.random.rand(N)
	H = numpy.eye(N)
	Hv = numpy.dot(H,v)
	assert_array_almost_equal( Hv, hess_vec(0,x,v))

def test_vec_jac():
	N = 3 # dimension
	M = 2 # codimension
	A = numpy.array([[ 1./N +(n==m) for n in range(N)] for m in range(M)])
	def vector_f(x):
		return numpy.dot(A,x)
		
	x = numpy.array([1.*n for n in range(N)])
	ax = adouble(x)
	
	trace_on(1)
	independent(ax)
	ay = vector_f(ax)
	dependent(ay)
	trace_off()
	u = numpy.random.rand(M)
	uJ = numpy.dot(u,A)
	assert_array_almost_equal( uJ, vec_jac(1,x,u, 0))


def test_jac_vec():
	N = 3 # dimension
	M = 2 # codimension
	A = numpy.array([[ 1./N +(n==m) for n in range(N)] for m in range(M)])
	def vector_f(x):
		return numpy.dot(A,x)
		
	x = numpy.array([1.*n for n in range(N)])
	ax = adouble(x)
	
	trace_on(1)
	independent(ax)
	ay = vector_f(ax)
	dependent(ay)
	trace_off()
	v = numpy.random.rand(N)
	Jv = numpy.dot(A,v)
	assert_array_almost_equal( Jv, jac_vec(1,x,v) )

def test_lagra_hess_vec():
	""" This test needs improvement: the result is always 0!!"""
	N = 3 # dimension
	M = 2 # codimension
	A = numpy.array([[ 1./N +(n==m) for n in range(N)] for m in range(M)])
	def vector_f(x):
		return numpy.dot(A,x)
		
	x = numpy.array([1.*n for n in range(N)])
	ax = adouble(x)
	
	trace_on(1)
	independent(ax)
	ay = vector_f(ax)
	dependent(ay)
	trace_off()
	u = numpy.random.rand(M)
	v = numpy.random.rand(N)
	assert_array_almost_equal(numpy.zeros(N,dtype=float), lagra_hess_vec(1,x,u,v) )

def test_jac_pat():
	N = 3 # dimension
	M = 2 # codimension
	def vector_f(x):
		return numpy.array([x[0]*x[1],x[1]*x[2]])

	x = numpy.array([1.*n +1. for n in range(N)])
	ax = adouble(x)
	
	trace_on(1)
	independent(ax)
	ay = vector_f(ax)
	dependent(ay)
	trace_off()

	options = numpy.array([1,1,0,0],dtype=int)
	pat = sparse.jac_pat(1,x,options)
	
	pat = numpy.asarray(pat,dtype=int)
	correct_pat = numpy.array([[0,1],[1,2]], dtype=int)
	assert_array_equal(pat, correct_pat)
	



def test_sparse_jac_no_repeat():
	N = 3 # dimension
	M = 2 # codimension
	def vector_f(x):
		return numpy.array([x[0]*x[1],x[1]*x[2]])

	x = numpy.array([1.*n +1. for n in range(N)])
	ax = adouble(x)
	
	trace_on(1)
	independent(ax)
	ay = vector_f(ax)
	dependent(ay)
	trace_off()

	options = numpy.array([1,1,0,0],dtype=int)
	result = sparse.sparse_jac_no_repeat(1,x,options)
	correct_nnz = 4
	correct_rind   = numpy.array([0,0,1,1])
	corrent_cind   = numpy.array([0,1,1,2])
	correct_values = numpy.array([2.,1.,3.,2.])

	assert_equal(result[0], correct_nnz)
	assert_array_equal(result[1], correct_rind)
	assert_array_equal(result[2], corrent_cind)
	assert_array_almost_equal(result[3], correct_values)

def test_sparse_jac_with_repeat():
	N = 3 # dimension
	M = 2 # codimension
	def vector_f(x):
		return numpy.array([x[0]*x[1],x[1]*x[2]])

	x = numpy.array([1.*n +1. for n in range(N)])
	ax = adouble(x)
	
	trace_on(1)
	independent(ax)
	ay = vector_f(ax)
	dependent(ay)
	trace_off()

	options = numpy.array([1,1,0,0],dtype=int)

	# first call
	result = sparse.sparse_jac_no_repeat(1,x,options)

	# second call
	x = numpy.array([1.*n +2. for n in range(N)])
	result = sparse.sparse_jac_repeat(1,x, result[0], result[1], result[2], result[3])

	correct_nnz = 4
	correct_rind   = numpy.array([0,0,1,1])
	corrent_cind   = numpy.array([0,1,1,2])
	correct_values = numpy.array([3.,2.,4.,3.])

	assert_equal(result[0], correct_nnz)
	assert_array_equal(result[1], correct_rind)
	assert_array_equal(result[2], corrent_cind)
	assert_array_almost_equal(result[3], correct_values)

def test_hess_pat():
	N = 3 # dimension
	
	def scalar_f(x):
		return x[0]*x[1] + x[1]*x[2] + x[2]*x[0]

	x = numpy.array([1.*n +1. for n in range(N)])
	ax = adouble(x)
	
	trace_on(1)
	independent(ax)
	ay = scalar_f(ax)
	dependent(ay)
	trace_off()

	option = 0
	pat = sparse.hess_pat(1,x,option)
	pat = numpy.asarray(pat,dtype=int)

	correct_pat = numpy.array([[1,2],[0,2], [0,1]], dtype=int)
	assert_array_equal(pat, correct_pat)


def test_sparse_hess_no_repeat():
	N1 = 3 # dimension
	def scalar_f(x):
		return x[0]*x[1] + x[1]*x[2] + x[2]*x[0]
		
	def scalar_f2(x):
		return x[0] * x[3] * (x[0] + x[1] + x[2]) + x[2]

	x1 = numpy.array([1.*n +1. for n in range(N1)])
	ax1 = adouble(x1)
	
	trace_on(1)
	independent(ax1)
	ay = scalar_f(ax1)
	dependent(ay)
	trace_off()

	options = numpy.array([0,0],dtype=int)
	result = sparse.sparse_hess_no_repeat(1, x1, options)
	correct_nnz = 3

	correct_rind   = numpy.array([0,0,1])
	corrent_cind   = numpy.array([1,2,2])
	correct_values = numpy.array([1.,1.,1.])

	assert_equal(result[0], correct_nnz)
	assert_array_equal(result[1], correct_rind)
	assert_array_equal(result[2], corrent_cind)
	assert_array_almost_equal(result[3], correct_values)
	

	N2 = 4
	x2 = numpy.array([1.*n +1. for n in range(N2)])
	
	trace_on(2)
	ax2 = adouble(x2)
	independent(ax2)
	ay = scalar_f2(ax2)
	dependent(ay)
	trace_off()
	
	options = numpy.array([0,0],dtype=int)
	for i in range(10):
		result = sparse.sparse_hess_no_repeat(2, x2, options)


	


def test_sparse_hess_repeat():
	N = 3 # dimension
	
	def scalar_f(x):
		return x[0]**3 + x[0]*x[1] + x[1]*x[2] + x[2]*x[0]

	x = numpy.array([1.*n +1. for n in range(N)])
	ax = adouble(x)
	
	trace_on(1)
	independent(ax)
	ay = scalar_f(ax)
	dependent(ay)
	trace_off()

	options = numpy.array([1,1],dtype=int)

	# first call
	result = sparse.sparse_hess_no_repeat(1,x,options)

	# second call
	x = numpy.array([1.*n +2. for n in range(N)])
	result = sparse.sparse_hess_repeat(1,x, result[1], result[2], result[3])

	correct_nnz = 4

	correct_rind   = numpy.array([0,0,0,1])
	corrent_cind   = numpy.array([0,1,2,2])
	correct_values = numpy.array([6*x[0],1.,1.,1.])

	assert_equal(result[0], correct_nnz)
	assert_array_equal(result[1], correct_rind)
	assert_array_equal(result[2], corrent_cind)
	assert_array_almost_equal(result[3], correct_values)

def test_repeated_taping():
	R = 20 # number of repetitions of the taping
	
	N = 3 # dimension
	M = 2 # codimension
	A = numpy.array([[ 1./N +(n==m) for n in range(N)] for m in range(M)])
	def vector_f(x):
		return numpy.dot(A,x)
		
	x = numpy.array([1.*n for n in range(N)])
	ax = adouble(x)
	
	for r in range(R):
		trace_on(1)
		independent(ax)
		ay = vector_f(ax)
		dependent(ay)
		trace_off()
		u = numpy.random.rand(M)
		uJ = numpy.dot(u,A)
		assert_array_almost_equal( uJ, vec_jac(1,x,u, 0))
		
	for r in range(R):
		trace_on(r)
		independent(ax)
		ay = vector_f(ax)
		dependent(ay)
		trace_off()
		u = numpy.random.rand(M)
		uJ = numpy.dot(u,A)
		assert_array_almost_equal( uJ, vec_jac(r,x,u, 0))		
		
		
def test_hov_forward():
	""" checks only first order"""
	N = 3
	P = 1
	D = 1
	epsilon1 =  numpy.sqrt(10**-16)
	
	def f(x):
		return numpy.array([x[0]*x[1] + x[0]*x[2], x[1]*x[2]])
		
	x = numpy.array([1.,2.,3.])
	ax = adouble(x)
	trace_on(1)
	independent(ax)
	ay = f(ax)
	dependent(ay)
	trace_off()
	x = numpy.random.rand(N)
	V = numpy.random.rand(N,P,D)
	
	(y,W) = hov_forward(1, x, V)
	
	W2 = (f(x+epsilon1*V[:,0,0]) - f(x))/epsilon1
	W2 = W2.reshape((2,P,D))
	
	assert_array_almost_equal(y, f(x))
	assert_array_almost_equal(W, W2)
	

def test_sparse_problem():
	return 0
	import scipy.sparse
	
	nvar = 4
	ncon = 2

	def eval_f(x, user_data = None):
		assert len(x) == 4
		return x[0] * x[3] * (x[0] + x[1] + x[2]) + x[2]

	def eval_grad_f(x, user_data = None):
		assert len(x) == 4
		grad_f = numpy.array([
			x[0] * x[3] + x[3] * (x[0] + x[1] + x[2]) ,
			x[0] * x[3],
			x[0] * x[3] + 1.0,
			x[0] * (x[0] + x[1] + x[2])
			])
		return grad_f;
		
	def eval_g(x, user_data= None):
		assert len(x) == 4
		return numpy.array([
			x[0] * x[1] * x[2] * x[3], 
			x[0]*x[0] + x[1]*x[1] + x[2]*x[2] + x[3]*x[3]
		])

	nnzj = 8
	def eval_jac_g(x, flag, user_data = None):
		if flag:
			return (numpy.array([0, 0, 0, 0, 1, 1, 1, 1]), 
				numpy.array([0, 1, 2, 3, 0, 1, 2, 3]))
		else:
			assert len(x) == 4
			return numpy.array([ x[1]*x[2]*x[3], 
						x[0]*x[2]*x[3], 
						x[0]*x[1]*x[3], 
						x[0]*x[1]*x[2],
						2.0*x[0], 
						2.0*x[1], 
						2.0*x[2], 
						2.0*x[3] ])
			
	nnzh = 10
	def eval_h(x, lagrange, obj_factor, flag, user_data = None):
		if flag:
			hrow = [0, 1, 1, 2, 2, 2, 3, 3, 3, 3]
			hcol = [0, 0, 1, 0, 1, 2, 0, 1, 2, 3]
			return (numpy.array(hcol,dtype=int), numpy.array(hrow,dtype=int))
		else:
			values = numpy.zeros((10), numpy.float_)
			values[0] = obj_factor * (2*x[3])
			values[1] = obj_factor * (x[3])
			values[2] = 0
			values[3] = obj_factor * (x[3])
			values[4] = 0
			values[5] = 0
			values[6] = obj_factor * (2*x[0] + x[1] + x[2])
			values[7] = obj_factor * (x[0])
			values[8] = obj_factor * (x[0])
			values[9] = 0
			values[1] += lagrange[0] * (x[2] * x[3])

			values[3] += lagrange[0] * (x[1] * x[3])
			values[4] += lagrange[0] * (x[0] * x[3])

			values[6] += lagrange[0] * (x[1] * x[2])
			values[7] += lagrange[0] * (x[0] * x[2])
			values[8] += lagrange[0] * (x[0] * x[1])
			values[0] += lagrange[1] * 2
			values[2] += lagrange[1] * 2
			values[5] += lagrange[1] * 2
			values[9] += lagrange[1] * 2
			return values


	x0 = numpy.array([1.0, 5.0, 5.0, 1.0])

	# check that adolc gives the same answers as derivatives calculated by hand
	trace_on(1)
	ax = adouble(x0)
	independent(ax)
	ay = eval_f(ax)
	dependent(ay)
	trace_off()

	trace_on(2)
	ax = adouble(x0)
	independent(ax)
	ay = eval_g(ax)
	dependent(ay)
	trace_off()
	
	trace_on(3)
	ax = adouble(x0)
	independent(ax)
	ay = eval_g(ax)
	dependent(ay[0])
	trace_off()
	
	trace_on(4)
	ax = adouble(x0)
	independent(ax)
	ay = eval_g(ax)
	dependent(ay[1])
	trace_off()
	

	def eval_f_adolc(x, user_data = None):
		 return function(1,x)[0]

	def eval_grad_f_adolc(x, user_data = None):
		 return gradient(1,x)

	def eval_g_adolc(x, user_data= None):
		return function(2,x)

	def eval_jac_g_adolc(x, flag, user_data = None):
		options = numpy.array([1,1,0,0],dtype=int)
		result = sparse.sparse_jac_no_repeat(2,x,options)
		if flag:
			return (numpy.asarray(result[1],dtype=int), numpy.asarray(result[2],dtype=int))
		else:
			return result[3]
			
	def eval_h_adolc(x, lagrange, obj_factor, flag, user_data = None):
		options = numpy.array([0,0],dtype=int)
		assert numpy.ndim(x) == 1
		assert numpy.size(x) == 4
		result_f = sparse.sparse_hess_no_repeat(1, x, options)
		result_g0 = sparse.sparse_hess_no_repeat(3, x,options)
		result_g1 = sparse.sparse_hess_no_repeat(4, x,options)
		Hf  = scipy.sparse.coo_matrix( (result_f[3], (result_f[1], result_f[2])), shape=(4, 4))
		Hg0 = scipy.sparse.coo_matrix( (result_g0[3], (result_g0[1], result_g0[2])), shape=(4, 4))
		Hg1 = scipy.sparse.coo_matrix( (result_g1[3], (result_g1[1], result_g1[2])), shape=(4, 4))
		
		H = Hf + Hg0 + Hg1
		H = H.tocoo()
		
		if flag:
			hrow = H.row
			hcol = H.col
			return (numpy.array(hcol,dtype=int), numpy.array(hrow,dtype=int))

		else:
			values = numpy.zeros((10), float)
			values[:] = H.data
			return values

	# function of f
	assert_almost_equal(eval_f(x0), eval_f_adolc(x0))
	
	# gradient of f
	assert_array_almost_equal(eval_grad_f(x0), eval_grad_f_adolc(x0))

	# function of g
	assert_array_almost_equal(eval_g(x0), function(2,x0))

	# sparse jacobian of g
	assert_array_equal(eval_jac_g_adolc(x0,True)[0], eval_jac_g(x0,True)[0])
	assert_array_equal(eval_jac_g_adolc(x0,True)[1], eval_jac_g(x0,True)[1])
	assert_array_equal(eval_jac_g_adolc(x0,False),  eval_jac_g(x0,False))
	
	# sparse hessian of the lagrangian
	lagrange = numpy.ones(2,dtype=float)
	obj_factor = 1.
	x0 = numpy.random.rand(4)
	result       = (eval_h(x0, lagrange, obj_factor, False), eval_h(x0, lagrange, obj_factor, True))
	result_adolc = (eval_h_adolc(x0, lagrange, obj_factor, False), eval_h_adolc(x0, lagrange, obj_factor, True))
	H       = scipy.sparse.coo_matrix( result, shape=(4, 4))
	H_adolc = scipy.sparse.coo_matrix( result_adolc, shape=(4, 4))
	H = H.todense()
	H_adolc = H_adolc.todense()
	assert_array_almost_equal( H, H_adolc.T)


	



	
	
#def test_gradient_and_jacobian_and_hessian():
	#N = 6 # dimension
	#M = 5 # codimension
	#P = 4 # number of directional derivatives
	#Q = 3 # number of adjoint derivatives
	#D = 2 # order of derivatives

	#A = numpy.array([[ 1./N +(n==m) for n in range(N)] for m in range(M)])
	#x = numpy.array([1./(i+1) for i in range(N)])
	#y = numpy.zeros(M)
	#u = numpy.zeros(M); u[0] = 1.
	#v = numpy.zeros(N); v[0] = 1.
	#Vnp = numpy.array([[n==p for  p in range(P)]for n in range(N)], dtype=float)
	#Vnd = numpy.array([[n==d and d==0 for d in range(D)]for n in range(N)], dtype=float)
	#Vnpd = numpy.array([[[ n==p and d == 0 for d in range(D)] for p in range(P)] for n in range(N)], dtype = float)
	#Uqm = numpy.array([[q==n for m in range(M)]for q in range(Q)], dtype=float)

	#b = numpy.zeros(N,dtype=float)
	#ax = numpy.array([adouble(1.) for i in range(N)])

	#def scalar_f(x):
		#return numpy.dot(x,x)

	#def vector_f(x):
		#return numpy.dot(A,x)

	#trace_on(0)
	#independent(ax)
	#ay = scalar_f(ax)
	#dependent(ay)
	#trace_off()

	#trace_on(1)
	#independent(ax)
	#ay = vector_f(ax)
	#dependent(ay)
	#trace_off()

	## basic drivers
	#assert_almost_equal(function(0,x)[0],scalar_f(x))
	#y = 2*x #gradient of scalar_f
	#print 'Gradient evaluation correct?\t\t',near_equal_with_num_error_increase(gradient(0,x), y)
	#H = 2*numpy.eye(N) #hessian of scalar_f
	#print 'Hessian evaluation correct?\t\t', near_equal_with_num_error_increase(hessian(0,x), H)
	#Hv = numpy.dot(H,v)
	#print 'Hess_vec evaluation correct?\t\t', near_equal_with_num_error_increase(hess_vec(0,x,v), Hv)
	#print 'Jacobian evaluation correct?\t\t', near_equal_with_num_error_increase(jacobian(1,x), A )
	#uJ = numpy.dot(u,A)
	#print 'vec_jac evaluation correct?\t\t', near_equal_with_num_error_increase(vec_jac(1,x,u, 0), uJ )
	#Jv = numpy.dot(A,v)
	#print 'vec_jac evaluation correct?\t\t', near_equal_with_num_error_increase(jac_vec(1,x,v), Jv )
	#print 'lagra_hess_vec evaluation correct?\t', near_equal_with_num_error_increase(lagra_hess_vec(1,x,v,u), numpy.zeros(N,dtype=float) )

	## low level functions
	#print 'zos_forward correct?\t\t\t', near_equal_with_num_error_increase(zos_forward(1,x,0), vector_f(x))
	#print 'fos_forward correct?\t\t\t', near_equal_with_num_error_increase(fos_forward(1,x,v,0)[1], A[:,0])
	#print 'fov_forward correct?\t\t\t', near_equal_with_num_error_increase(fov_forward(1,x,Vnp)[1], A[:,:P])
	#print 'hov_forward correct?\t\t\t', near_equal_with_num_error_increase(hov_forward(1,D,x,Vnpd)[1][:,:,-1], numpy.zeros((M,P)))
	#uA = numpy.dot(u,A)
	#print 'fos_reverse correct?\t\t\t', near_equal_with_num_error_increase(fos_reverse(1,u), uA)
	#UqmA = numpy.dot(Uqm,A)
	#print 'fov_reverse correct?\t\t\t', near_equal_with_num_error_increase(fov_reverse(1,Uqm), UqmA)
	#print 'hos_forward correct?\t\t\t', near_equal_with_num_error_increase(hos_forward(1,D,x, Vnd,D+1)[1][:,-1], numpy.zeros(M))
	#print 'hos_reverse correct?\t\t\t', near_equal_with_num_error_increase(hos_reverse(1,D,u)[:,-1], numpy.zeros(N))
	#print 'hov_reverse correct?\t\t\t', near_equal_with_num_error_increase(hov_reverse(1,D,Uqm)[0][:,:,-1], numpy.zeros((Q,N)))



## c style functions
#y = numpy.zeros(1, dtype=float)
#g = numpy.zeros(N, dtype=float)
#H = numpy.zeros((N,N), dtype=float)
#z = numpy.zeros(N, dtype=float)

#function(0,1,N,x,y)
#gradient(0,N,x,g)
#hessian(0,N,x,H)
#hess_vec(0, N, x,v, z)



#print 'number of failed tests =',number_of_errors




## operator / for int and double
#test_expression('a / 2: ',	lambda x: x[0]/x[1], (a,2),		(a.val,2))
#test_expression('a / 2.:',	lambda x: x[0]/x[1], (a,2.),	(a.val,2.))
#test_expression('2 / a: ',	lambda x: x[0]/x[1], (2,a),		(2,a.val))
#test_expression('2./ a.:',	lambda x: x[0]/x[1], (2.,a),	(2., a.val))

##operator +,-,*,/ for badouble
#test_expression('a + b: ',	lambda x: x[0]+x[1], (a,b),		(a.val,b.val))
#test_expression('a - b: ',	lambda x: x[0]-x[1], (a,b),		(a.val,b.val))
#test_expression('a * b: ',	lambda x: x[0]*x[1], (a,b),		(a.val,b.val))
#test_expression('a / b: ',	lambda x: x[0]/x[1], (a,b),		(a.val,b.val))

## operator +=,-=,*=,/= for badouble
#c = adouble(a)
#d = c.val
#c+=b; d+=b.val; print 'c+=b  \t ',c,'==',d,near_equal_with_num_error_increase(c.val,d)
#c-=b; d-=b.val; print 'c-=b  \t ',c,'==',d,near_equal_with_num_error_increase(c.val,d)
#c*=b; d*=b.val; print 'c*=b  \t ',c,'==',d,near_equal_with_num_error_increase(c.val,d)
#c/=b; d/=b.val; print 'c/=b  \t ',c,'==',d,near_equal_with_num_error_increase(c.val,d)

## operator +=,-=,*=,/= for badouble
#c = adouble(a)
#d = c.val
#c+=b.val; d+=b.val; print 'c+=b  \t ',c,'==',d,near_equal_with_num_error_increase(c.val,d)
#c-=b.val; d-=b.val; print 'c-=b  \t ',c,'==',d,near_equal_with_num_error_increase(c.val,d)
#c*=b.val; d*=b.val; print 'c*=b  \t ',c,'==',d,near_equal_with_num_error_increase(c.val,d)
#c/=b.val; d/=b.val; print 'c/=b  \t ',c,'==',d,near_equal_with_num_error_increase(c.val,d)

## operator **
#test_expression('a**2: ',	lambda x: x**2, a,		a.val)
#print "to be implemented print '2.**a', 2.**a"


##functions
#import numpy as numpy
#a = adouble(0.4);	print 'a=adouble(13.)\t= ',a,'\t\ta.val =',a.val
#test_expression('exp  (a)     : ',		lambda x: numpy.exp  (x),  a,		a.val)
#test_expression('log  (a)     : ',		lambda x: numpy.log  (x),  a,		a.val)
#test_expression('sqrt (a)     : ',		lambda x: numpy.sqrt (x),  a,		a.val)
#test_expression('sin  (a)     : ',		lambda x: numpy.sin  (x),  a,		a.val)
#test_expression('cos  (a)     : ',		lambda x: numpy.cos  (x),  a,		a.val)
#test_expression('tan  (a)     : ',		lambda x: numpy.tan  (x),  a,		a.val)
#test_expression('asin (a)     : ',		lambda x: numpy.arcsin (x),  a,		a.val)
#test_expression('acos (a)     : ',		lambda x: numpy.arccos (x),  a,		a.val)
#test_expression('atan (a)     : ',		lambda x: numpy.arctan (x),  a,		a.val)
#test_expression('log10(a)     : ',		lambda x: numpy.log10(x),  a,		a.val)
#test_expression('sinh (a)     : ',		lambda x: numpy.sinh (x),  a,		a.val)
#test_expression('cosh (a)     : ',		lambda x: numpy.cosh (x),  a,		a.val)
#test_expression('tanh (a)     : ',		lambda x: numpy.tanh (x),  a,		a.val)
#test_expression('fabs (a)     : ',		lambda x: numpy.fabs (x),  a,		a.val)
#test_expression('ceil (a)     : ',		lambda x: numpy.ceil (x),  a,		a.val)
#test_expression('floor(a)    : ',		lambda x: numpy.floor(x),	 a,		a.val)

##print 'exp  (a)', numpy.exp  (a), a.exp  ()
##print 'log  (a)', numpy.log  (a), a.log  ()
##print 'sqrt (a)', numpy.sqrt (a), a.sqrt ()
##print 'sin  (a)', numpy.sin  (a), a.sin  ()
##print 'cos  (a)', numpy.cos  (a), a.cos  ()
##print 'tan  (a)', numpy.tan  (a), a.tan  ()
##print 'asin (a)', numpy.arcsin(a),a.asin ()
##print 'acos (a)', numpy.arccos(a),a.acos ()
##print 'atan (a)', numpy.arctan(a),a.atan ()
##print 'log10(a)', numpy.log10(a), a.log10()
##print 'sinh (a)', numpy.sinh (a), a.sinh ()
##print 'cosh (a)', numpy.cosh (a), a.cosh ()
##print 'tanh (a)', numpy.tanh (a), a.tanh ()
##print 'fabs (a)', numpy.fabs (a), a.fabs ()
##print 'ceil (a)', numpy.ceil (a), a.ceil ()
##print 'floor (a)',numpy.floor (a),a.floor ()
#print 'fmax (a,b)',			    a.fmax (b)
#print 'fmax (a,0.3)',			a.fmax (0.3)
#print 'fmax (0.3,a)','/* not implemented */'
#print 'fmin (a,b)',			    a.fmin (b)
#print 'fmin (a,0.3)',			a.fmin (0.3)
#print 'fmin (0.3,a)','/* not implemented */'





try:
	import nose
except:
	print 'Please install nose for unit testing'

if __name__ == '__main__':
    nose.runmodule()

