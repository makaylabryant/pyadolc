#ifndef AP_HPP
#define AP_HPP
#define PY_ARRAY_UNIQUE_SYMBOL PyArrayHandle

#include "num_util.h"
#include "adolc.h"

using namespace std;
namespace b = boost;
namespace bp = boost::python;
namespace bpn = boost::python::numeric;
namespace nu = num_util;


int get_size_of_short(){ return static_cast<int>(sizeof(short)); }
int get_size_of_int(){ return static_cast<int>(sizeof(int)); }
int get_size_of_long(){ return static_cast<int>(sizeof(long)); }


extern adub exp		( const badouble& );
extern adub log		( const badouble& );
extern adub sqrt	( const badouble& );
extern adub sin		( const badouble& );
extern adub cos		( const badouble& );
extern adub tan		( const badouble& );
extern adub asin	( const badouble& );
extern adub acos	( const badouble& );
extern adub atan	( const badouble& );
extern adub pow		( const badouble&, double );
extern adouble pow	( const badouble&, const badouble& );
extern adouble pow	( double, const badouble& ); /*this one doesnt work correctly yet */
extern adub log10	( const badouble& );
extern adub sinh  ( const badouble& );
extern adub cosh  ( const badouble& );
extern adub tanh  ( const badouble& );
extern adub asinh ( const badouble& );
// extern adub /*acosh*/ ( const badouble& );
// extern adub atanh ( const badouble& );
extern adub fabs  ( const badouble& );
extern adub ceil  ( const badouble& );
extern adub floor ( const badouble& );
extern adub fmax ( const badouble&, const badouble& );
extern adub fmax ( double, const badouble& );
extern adub fmax ( const badouble&, double );
extern adub fmin ( const badouble&, const badouble& );
extern adub fmin ( double, const badouble& );
extern adub fmin ( const badouble&, double );
extern adub ldexp ( const badouble&, int );
// extern adub frexp ( const badouble&, int* );
// extern adub erf   ( const badouble& );

/* THIN WRAPPER FOR OVERLOADED FUNCTIONS */
void trace_on_default_argument(short tape_tag){ trace_on(tape_tag,0);}
void trace_off_default_argument(){ trace_off(0);}

// /* PYTHONIC CALLS OF FUNCTIONS */
// bpn::array	wrapped_function			(short tape_tag, bpn::array &bpn_x);
// bpn::array	wrapped_gradient			(short tape_tag, bpn::array &bpn_x);
// bpn::array	wrapped_hessian				(short tape_tag, bpn::array &bpn_x);
// bpn::array	wrapped_jacobian			(short tape_tag, bpn::array &bpn_x);
// bpn::array	wrapped_vec_jac				(short tape_tag, bpn::array &bpn_x, bpn::array &bpn_u, bool repeat);
// bpn::array	wrapped_jac_vec				(short tape_tag, bpn::array &bpn_x, bpn::array &bpn_v);
// bpn::array	wrapped_hess_vec			(short tape_tag, bpn::array &bpn_x, bpn::array &bpn_v);
// bpn::array	wrapped_lagra_hess_vec		(short tape_tag, bpn::array &bpn_x, bpn::array &bpn_u, bpn::array &bpn_v);
// // void		wrapped_jac_solv			(short tape_tag, bpn::array &bpn_x, bpn::array &bpn_b, int sparse, int mode);
// bpn::array	wrapped_zos_forward			(short tape_tag, bpn::array &bpn_x, int keep);
// bp::tuple	wrapped_fos_forward			(short tape_tag, bpn::array &bpn_x, bpn::array &bpn_v, int keep);
// bp::tuple 	wrapped_fov_forward			(short tape_tag, bpn::array &bpn_x, bpn::array &bpn_V);
// bp::tuple	wrapped_hos_forward			(short tape_tag, bpn::array &bpn_x, bpn::array &bpn_V, int keep);
// bp::tuple	wrapped_hov_forward			(short tape_tag, bpn::array &bpn_x, bpn::array &bpn_V);
// bp::tuple	wrapped_hov_wk_forward		(short tape_tag, bpn::array &bpn_x, bpn::array &bpn_V, int keep);
// bpn::array wrapped_fos_reverse			(short tape_tag, bpn::array &bpn_u);
// bpn::array wrapped_fov_reverse			(short tape_tag, bpn::array &bpn_U);
// bpn::array wrapped_hos_reverse			(short tape_tag, int D, bpn::array &bpn_u);
// bp::tuple wrapped_hov_reverse			(short tape_tag, int D, bpn::array &bpn_U);
// bp::tuple wrapped_hov_ti_reverse		(short tape_tag, bpn::array &bpn_U);


/* C STYLE CALLS OF FUNCTIONS */
void c_wrapped_function			(short tape_tag, int M, int N, bpn::array &bpn_x, bpn::array &bpn_y );
void c_wrapped_gradient			(short tape_tag, int N, bpn::array &bpn_x, bpn::array &bpn_g);
void c_wrapped_hessian			(short tape_tag, int N, bpn::array &bpn_x, bpn::array &bpn_H);
void c_wrapped_jacobian			(short tape_tag, int M, int N, bpn::array &bpn_x, bpn::array &bpn_J);
void c_wrapped_vec_jac			(short tape_tag, int M, int N, bool repeat, bpn::array &bpn_x, bpn::array &bpn_u, bpn::array &bpn_z);
void c_wrapped_jac_vec			(short tape_tag, int M, int N, bpn::array &bpn_x, bpn::array &bpn_v, bpn::array &bpn_z);
void c_wrapped_hess_vec			(short tape_tag, int N, bpn::array &bpn_x, bpn::array &bpn_v, bpn::array &bpn_z);
void c_wrapped_lagra_hess_vec	(short tape_tag, int M, int N, bpn::array &bpn_x, bpn::array &bpn_v, bpn::array &bpn_u,bpn::array &bpn_h);
// void c_wrapped_jac_solv			(short tape_tag, int N, bpn::array &bpn_x, bpn::array &bpn_b, int sparse, int mode);
void c_wrapped_zos_forward		(short tape_tag, int M, int N, int keep, bpn::array &bpn_x, bpn::array &bpn_y);
void c_wrapped_fos_forward		(short tape_tag, int M, int N, int keep, bpn::array &bpn_x, bpn::array &bpn_v, bpn::array &bpn_y, bpn::array &bpn_w);
void c_wrapped_fov_forward		(short tape_tag, int M, int N, int P, bpn::array &bpn_x, bpn::array &bpn_V, bpn::array &bpn_y, bpn::array &bpn_W);
void c_wrapped_hos_forward		(short tape_tag, int M, int N, int D, int keep, bpn::array &bpn_x, bpn::array &bpn_V, bpn::array &bpn_y, bpn::array &bpn_W);
void c_wrapped_hov_forward		(short tape_tag, int M, int N, int D, int P, bpn::array &bpn_x, bpn::array &bpn_V, bpn::array &bpn_y, bpn::array &bpn_W);
void c_wrapped_hov_wk_forward	(short tape_tag, int M, int N, int D, int keep, int P, bpn::array &bpn_x, bpn::array &bpn_V, bpn::array &bpn_y, bpn::array &bpn_W);


void c_wrapped_fos_reverse		(short tape_tag, int M, int N, bpn::array &bpn_u, bpn::array &bpn_z);
void c_wrapped_fov_reverse		(short tape_tag, int M, int N, int Q, bpn::array &bpn_U, bpn::array &bpn_Z);
void c_wrapped_hos_reverse		(short tape_tag, int M, int N, int D, bpn::array &bpn_u, bpn::array &bpn_Z);
void c_wrapped_hov_reverse		(short tape_tag, int M, int N, int D, int Q, bpn::array &bpn_U, bpn::array &bpn_Z, bpn::array &bpn_nz);
void c_wrapped_hov_ti_reverse	(short tape_tag, int M, int N, int D, int Q, bpn::array &bpn_U, bpn::array &bpn_Z, bpn::array &bpn_nz);


void py_tape_doc(short tape_tag, bpn::array &bpn_x, bpn::array &bpn_y );
bp::dict wrapped_tapestats(short tape_tag);

/* of class badouble */
adub	(*exp_adub) 		( const badouble& ) = &exp;
adub	(*log_adub) 		( const badouble& ) = &log;
adub	(*sqrt_adub)		( const badouble& ) = &sqrt;
adub	(*sin_adub) 		( const badouble& ) = &sin;
adub	(*cos_adub) 		( const badouble& ) = &cos;
adub	(*tan_adub) 		( const badouble& ) = &tan;
adub	(*asin_adub)		( const badouble& ) = &asin;
adub	(*acos_adub)		( const badouble& ) = &acos;
adub	(*atan_adub)		( const badouble& ) = &atan;
adub	(*log10_adub)		( const badouble& ) = &log10;
adub	(*sinh_adub)		( const badouble& ) = &sinh;
adub	(*cosh_adub) 		( const badouble& ) = &cosh;
adub	(*tanh_adub) 		( const badouble& ) = &tanh;
// adub    (*asinh_adub) 		( const badouble& ) = &asinh;
// adub    (*acosh_adub) 		( const badouble& ) = &acosh;
// adub    (*atanh_adub) 		( const badouble& ) = &atanh;
adub	(*fabs_adub) 		( const badouble& ) = &fabs;
adub	(*ceil_adub)		( const badouble& ) = &ceil;
adub	(*floor_adub) 		( const badouble& ) = &floor;

adub	(*pow_adub)                       ( const badouble&, double ) = &pow;
adouble	(*pow_adouble_badouble_badouble)  ( const badouble&, const badouble& ) = &pow;
adouble (*pow_adouble_double_badouble)    ( double, const badouble& ) = &pow;
adub	(*fmax_adub_badouble_badouble)    ( const badouble&, const badouble& ) = &fmax;
adub	(*fmax_adub_double_badouble)      ( double, const badouble& ) = &fmax;
adub	(*fmax_adub_badouble_double)      ( const badouble&, double ) = &fmax;
adub	(*fmin_adub_badouble_badouble)    ( const badouble&, const badouble& ) = &fmin;
adub	(*fmin_adub_double_badouble)      ( double, const badouble& ) = &fmin;
adub	(*fmin_adub_badouble_double)      ( const badouble&, double ) = &fmin;
adub	(*ldexp_adub) 		( const badouble&, int ) = &ldexp;
// adub (*frexp_adub) 		( const badouble&, int* ) = &frexp;
// adub (*erf_adub) 		( const badouble& ) = &erf;

/* WRAPPED OPERATORS */
/* unary */
adub *adub_neg_badouble   (const badouble &rhs){	return new adub(operator*(-1.,rhs));}
adub *adub_exp_badouble   (const badouble &rhs){	return new adub(exp(rhs));}
adub *adub_log_badouble   (const badouble &rhs){	return new adub(log(rhs));}
adub *adub_sin_badouble   (const badouble &rhs){	return new adub(sin(rhs));}
adub *adub_cos_badouble   (const badouble &rhs){	return new adub(cos(rhs));}
adub *adub_tan_badouble   (const badouble &rhs){	return new adub(tan(rhs));}
adub *adub_asin_badouble  (const badouble &rhs){	return new adub(asin(rhs));}
adub *adub_acos_badouble  (const badouble &rhs){	return new adub(acos(rhs));}
adub *adub_atan_badouble  (const badouble &rhs){	return new adub(atan(rhs));}
adub *adub_sqrt_badouble  (const badouble &rhs){	return new adub(sqrt(rhs));}
adub *adub_sinh_badouble  (const badouble &rhs){	return new adub(sinh(rhs));}
adub *adub_cosh_badouble  (const badouble &rhs){	return new adub(cosh(rhs));}
adub *adub_tanh_badouble  (const badouble &rhs){	return new adub(tanh(rhs));}
// adub *adub_asinh_badouble  (const badouble &rhs){	return new adub(asinh(rhs));}
// adub *adub_acosh_badouble  (const badouble &rhs){	return new adub(acosh(rhs));}
// adub *adub_atanh_badouble  (const badouble &rhs){	return new adub(atanh(rhs));}


adub *adub_fabs_badouble  (const badouble &rhs){	return new adub(fabs(rhs));}
adub *adub_ceil_badouble  (const badouble &rhs){	return new adub(ceil(rhs));}
adub *adub_floor_badouble (const badouble &rhs){	return new adub(floor(rhs));}
adub *adub_log10_badouble (const badouble &rhs){	return new adub(log10(rhs));}

/* binary */
adub *adub_add_badouble_badouble(const badouble &lhs, const badouble &rhs){	return new adub(operator+(lhs,rhs));}
adub *adub_sub_badouble_badouble(const badouble &lhs, const badouble &rhs){	return new adub(operator-(lhs,rhs));}
adub *adub_mul_badouble_badouble(const badouble &lhs, const badouble &rhs){	return new adub(operator*(lhs,rhs));}
adub *adub_div_badouble_badouble(const badouble &lhs, const badouble &rhs){	return new adub(operator/(lhs,rhs));}

adub *adub_add_badouble_double(const badouble &lhs,double rhs){	return new adub(operator+(lhs,rhs));}
adub *adub_sub_badouble_double(const badouble &lhs,double rhs){	return new adub(operator-(lhs,rhs));}
adub *adub_mul_badouble_double(const badouble &lhs,double rhs){	return new adub(operator*(lhs,rhs));}
adub *adub_div_badouble_double(const badouble &lhs,double rhs){	return new adub(operator/(lhs,rhs));}

adub *adub_add_double_badouble(const badouble &rhs,double lhs){	return new adub(operator+(lhs,rhs));}
adub *adub_sub_double_badouble(const badouble &rhs,double lhs){	return new adub(operator-(lhs,rhs));}
adub *adub_mul_double_badouble(const badouble &rhs,double lhs){	return new adub(operator*(lhs,rhs));}
adub *adub_div_double_badouble(const badouble &rhs,double lhs){	return new adub(operator/(lhs,rhs));}


adub *adub_pow_badouble_double  (const badouble &lhs, const double &rhs)  {	return new adub(pow(lhs,rhs));}
adouble *adouble_pow_badouble_badouble(const badouble &lhs, const badouble &rhs){	return new adouble(pow(lhs,rhs));}
adouble *adouble_pow_double_badouble(const badouble &rhs, double lhs){	return new adouble(pow(lhs,rhs));}




double depends_on(badouble &a){
	double coval;
	a.operator>>=(coval);
	return coval;
}

badouble& (badouble::*operator_eq_double) ( double ) = &badouble::operator=;
badouble& (badouble::*operator_eq_badouble) ( const badouble& ) = &badouble::operator=;
badouble& (badouble::*operator_eq_adub) ( const adub& ) = &badouble::operator=;


BOOST_PYTHON_MODULE(_adolc)
{
	using namespace boost::python;
	import_array(); 										/* some kind of hack to get numpy working */
	bpn::array::set_module_and_type("numpy", "ndarray");	/* some kind of hack to get numpy working */
	
	scope().attr("__doc__") ="unused: moved docstring to adolc.py";
	
	def("get_size_of_short", get_size_of_short);
	def("get_size_of_int", get_size_of_int);
	def("get_size_of_long", get_size_of_long);
	

	def("trace_on",trace_on_default_argument);
	def("trace_off",trace_off_default_argument);

// 	def("function", 		&wrapped_function);
// 	def("gradient", 		&wrapped_gradient);
// 	def("hessian",			&wrapped_hessian);
// 	def("jacobian", 		&wrapped_jacobian);
// 	def("vec_jac",			&wrapped_vec_jac);
// 	def("jac_vec",			&wrapped_jac_vec);
// 	def("hess_vec",			&wrapped_hess_vec);
// 	def("lagra_hess_vec", 	&wrapped_lagra_hess_vec);

// 	def("zos_forward",		&wrapped_zos_forward);
// 	def("fos_forward",		&wrapped_fos_forward);
// 	def("fov_forward",		&wrapped_fov_forward);
// 	def("hos_forward",		&wrapped_hos_forward);
// 	def("hov_forward",		&wrapped_hov_forward);

// 	def("hov_wk_forward",	&wrapped_hov_wk_forward);
													
// 	def("fos_reverse",		&wrapped_fos_reverse);
     
// 	def("fov_reverse",		&wrapped_fov_reverse);
													
// 	def("hos_reverse",		&wrapped_hos_reverse);
// 	def("hov_reverse", 		&wrapped_hov_reverse);

// 	def("hov_ti_reverse", 	&wrapped_hov_ti_reverse);
													

	/* c style functions */
	def("function", 		&c_wrapped_function);
	def("gradient", 		&c_wrapped_gradient);
	def("hessian",			&c_wrapped_hessian);
	def("jacobian", 		&c_wrapped_jacobian);
	def("vec_jac",			&c_wrapped_vec_jac);
	def("jac_vec",			&c_wrapped_jac_vec);
	def("hess_vec",			&c_wrapped_hess_vec);
	def("lagra_hess_vec", 	&c_wrapped_lagra_hess_vec);
// 	def("jac_solv",			&c_wrapped_jac_solv); /* buggy ! */

	def("zos_forward",		&c_wrapped_zos_forward);
	def("fos_forward",		&c_wrapped_fos_forward);
	def("fov_forward",		&c_wrapped_fov_forward);
	def("hos_forward",		&c_wrapped_hos_forward);
	def("hov_forward",		&c_wrapped_hov_forward);
// 	def("hov_wk_forward",	&c_wrapped_hov_wk_forward);


	def("fos_reverse",		&c_wrapped_fos_reverse);
	def("fov_reverse",		&c_wrapped_fov_reverse);
	def("hos_reverse",		&c_wrapped_hos_reverse);
	def("hov_reverse", 		&c_wrapped_hov_reverse);
	def("hov_ti_reverse", 	&c_wrapped_hov_ti_reverse);
	
	def("depends_on", 		&depends_on);
	def("tape_to_latex",	py_tape_doc);

	def("tapestats", &wrapped_tapestats);

	def("exp",  adub_exp_badouble, return_value_policy<manage_new_object>()  );
	def("log",  adub_log_badouble, return_value_policy<manage_new_object>()  );
	def("sin", adub_sin_badouble, return_value_policy<manage_new_object>()  );
	def("cos", adub_cos_badouble, return_value_policy<manage_new_object>()  );	
	def("tan",  adub_tan_badouble, return_value_policy<manage_new_object>()  );
	def("asin", adub_asin_badouble, return_value_policy<manage_new_object>()  );
	def("acos", adub_acos_badouble, return_value_policy<manage_new_object>()  );
	def("atan", adub_atan_badouble, return_value_policy<manage_new_object>()  );
	def("sqrt", adub_sqrt_badouble, return_value_policy<manage_new_object>()  );
	def("sinh", adub_sinh_badouble, return_value_policy<manage_new_object>()  );
	def("cosh", adub_cosh_badouble, return_value_policy<manage_new_object>()  );
	def("fabs", adub_fabs_badouble, return_value_policy<manage_new_object>()  );
	def("ceil", adub_ceil_badouble, return_value_policy<manage_new_object>()  );
	def("floor", adub_floor_badouble, return_value_policy<manage_new_object>()  );
	def("log10", adub_log10_badouble, return_value_policy<manage_new_object>()  );


	class_<badouble>("badouble", init<const badouble &>())
			.def(boost::python::self_ns::str(self))

			.add_property("val", &badouble::value)
			.add_property("loc", &badouble::loc)
			
			.def("is_independent", &badouble::operator<<=, return_internal_reference<>())
			.def("__ilshift__", operator_eq_double, return_internal_reference<>())
			.def("__ilshift__", operator_eq_badouble, return_internal_reference<>())
			.def("__ilshift__", operator_eq_adub, return_internal_reference<>())

			.def("__irshift__", &badouble::operator>>=, return_internal_reference<>())


			.def(self += double() )
			.def(self -= double() )
			.def(self *= double() )
			.def(self /= double() )
            
            .def(self += int() )
            .def(self -= int() )
            .def(self *= int() )
            .def(self /= int() )            

			.def(self += self )
			.def(self -= self )
			.def(self *= self )
			.def(self /= self )

		
			.def(self < double() )
			.def(self <= double() )
			.def(self > double() )
			.def(self >= double() )
            
            .def(self < int() )
            .def(self <= int() )
            .def(self > int() )
            .def(self >= int() )            
            
		
			.def(self <  self  )
			.def(self <= self  )
			.def(self >  self  )
			.def(self >= self  )
			

// 			.def(-self)  using this unary operator somehow screws up LATER computations, i.e. the operator works correctly, but subsequent calculations screw up!!
// 			.def(+self)

			.def("__neg__", adub_neg_badouble, return_value_policy<manage_new_object>())		

			.def("__add__", adub_add_badouble_badouble, return_value_policy<manage_new_object>())
			.def("__sub__", adub_sub_badouble_badouble, return_value_policy<manage_new_object>())
			.def("__mul__", adub_mul_badouble_badouble, return_value_policy<manage_new_object>())
			.def("__div__", adub_div_badouble_badouble, return_value_policy<manage_new_object>())

			.def("__radd__", adub_add_double_badouble, return_value_policy<manage_new_object>())
			.def("__rsub__", adub_sub_double_badouble, return_value_policy<manage_new_object>())
			.def("__rmul__", adub_mul_double_badouble, return_value_policy<manage_new_object>())
			.def("__rdiv__", adub_div_double_badouble, return_value_policy<manage_new_object>())

			.def("__add__", adub_add_badouble_double, return_value_policy<manage_new_object>())
			.def("__sub__", adub_sub_badouble_double, return_value_policy<manage_new_object>())
			.def("__mul__", adub_mul_badouble_double, return_value_policy<manage_new_object>())
			.def("__div__", adub_div_badouble_double, return_value_policy<manage_new_object>())
                        
			.def("__pow__", adub_pow_badouble_double,   return_value_policy<manage_new_object>())
			.def("__pow__", adouble_pow_badouble_badouble, return_value_policy<manage_new_object>())
			.def("__rpow__",adouble_pow_double_badouble, return_value_policy<manage_new_object>())

			.def("exp",  adub_exp_badouble, return_value_policy<manage_new_object>()  )
			.def("log",  adub_log_badouble, return_value_policy<manage_new_object>()  )
			.def("sin", adub_sin_badouble, return_value_policy<manage_new_object>()  )
			.def("cos", adub_cos_badouble, return_value_policy<manage_new_object>()  )
			.def("tan",  adub_tan_badouble, return_value_policy<manage_new_object>()  )
			.def("arcsin", adub_asin_badouble, return_value_policy<manage_new_object>()  )
			.def("arccos", adub_acos_badouble, return_value_policy<manage_new_object>()  )
			.def("arctan", adub_atan_badouble, return_value_policy<manage_new_object>()  )
			.def("sqrt", adub_sqrt_badouble, return_value_policy<manage_new_object>()  )
			.def("sinh", adub_sinh_badouble, return_value_policy<manage_new_object>()  )
			.def("cosh", adub_cosh_badouble, return_value_policy<manage_new_object>()  )
			.def("tanh", adub_tanh_badouble, return_value_policy<manage_new_object>()  )
// 			.def("arcsinh", adub_asinh_badouble, return_value_policy<manage_new_object>()  )
// 			.def("acosh", adub_acosh_badouble, return_value_policy<manage_new_object>()  )
// 			.def("arctanh", adub_atanh_badouble, return_value_policy<manage_new_object>()  )
			.def("fabs", adub_fabs_badouble, return_value_policy<manage_new_object>()  )
			.def("abs", adub_fabs_badouble, return_value_policy<manage_new_object>()  )
			.def("ceil", adub_ceil_badouble, return_value_policy<manage_new_object>()  )
			.def("floor", adub_floor_badouble, return_value_policy<manage_new_object>()  )
			.def("log10", adub_log10_badouble, return_value_policy<manage_new_object>()  )
// 			.def("asinh",asinh_adub)
// 			.def("acosh",acosh_adub)
// 			.def("atanh",atanh_adub)
			.def("fmax", fmax_adub_badouble_badouble)
			.def("fmax", fmax_adub_double_badouble)
			.def("fmax", fmax_adub_badouble_double)
			.def("fmin", fmin_adub_badouble_badouble)
			.def("fmin", fmin_adub_double_badouble)
			.def("fmin", fmin_adub_badouble_double)
	;

	class_<adub, bases<badouble> >("adub", no_init)
// 			.def(init<locint>())
// 			.def(init<const adub &>())
	;

	class_<adouble, bases<badouble> >("adouble", init<double>())
			.def(init<const adouble&>())
			.def(init<const adub&>())
	;
}

#endif
