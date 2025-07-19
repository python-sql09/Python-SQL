// JaiMarketAuthSystem.js
import React, { useState } from 'react';
import { Mail, Lock, Eye, EyeOff, AlertCircle } from 'lucide-react';

const JaiMarketAuthSystem = () => {
  const [currentView, setCurrentView] = useState('signin');
  const [showPassword, setShowPassword] = useState(false);
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    email: '',
    password: '',
    confirmPassword: '',
    securityQuestion: '',
    securityAnswer: '',
    agreeToTerms: false
  });
  const [errors, setErrors] = useState({});

  const validateForm = () => {
    const newErrors = {};
    if (!formData.email.trim()) newErrors.email = 'Email is required';
    if (!formData.password) newErrors.password = 'Password is required';
    if (currentView === 'signup') {
      if (!formData.firstName) newErrors.firstName = 'First name required';
      if (!formData.lastName) newErrors.lastName = 'Last name required';
      if (formData.password !== formData.confirmPassword) newErrors.confirmPassword = 'Passwords do not match';
      if (!formData.securityQuestion) newErrors.securityQuestion = 'Select a security question';
      if (!formData.securityAnswer) newErrors.securityAnswer = 'Provide an answer';
      if (!formData.agreeToTerms) newErrors.agreeToTerms = 'Accept terms to continue';
    }
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleInputChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!validateForm()) return;
    alert(`${currentView === 'signin' ? 'Signed in' : 'Account created'} successfully!`);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-100 to-white flex items-center justify-center py-12 px-4">
      <div className="max-w-md w-full bg-white p-6 rounded-xl shadow-xl">
        <h1 className="text-3xl font-bold text-blue-700 text-center mb-4">Jai Market</h1>
        <h2 className="text-xl font-semibold text-center mb-6">
          {currentView === 'signin' ? 'Login to your account' : 'Sign Up for Jai Market'}
        </h2>

        {errors.general && <p className="text-red-600 mb-2 flex items-center"><AlertCircle size={16} /> {errors.general}</p>}

        <form onSubmit={handleSubmit} className="space-y-4">
          {currentView === 'signup' && (
            <div className="flex gap-2">
              <input name="firstName" type="text" placeholder="First Name" value={formData.firstName} onChange={handleInputChange} className="w-1/2 border p-2 rounded" />
              <input name="lastName" type="text" placeholder="Last Name" value={formData.lastName} onChange={handleInputChange} className="w-1/2 border p-2 rounded" />
            </div>
          )}

          <div className="relative">
            <Mail className="absolute left-2 top-2.5 text-gray-400" />
            <input name="email" type="email" placeholder="Email" value={formData.email} onChange={handleInputChange} className="pl-10 w-full border p-2 rounded" />
          </div>

          <div className="relative">
            <Lock className="absolute left-2 top-2.5 text-gray-400" />
            <input name="password" type={showPassword ? 'text' : 'password'} placeholder="Password" value={formData.password} onChange={handleInputChange} className="pl-10 pr-10 w-full border p-2 rounded" />
            <button type="button" onClick={() => setShowPassword(!showPassword)} className="absolute right-2 top-2.5 text-gray-500">
              {showPassword ? <EyeOff size={18} /> : <Eye size={18} />}
            </button>
          </div>

          {currentView === 'signup' && (
            <>
              <input name="confirmPassword" type="password" placeholder="Confirm Password" value={formData.confirmPassword} onChange={handleInputChange} className="w-full border p-2 rounded" />

              <select name="securityQuestion" value={formData.securityQuestion} onChange={handleInputChange} className="w-full border p-2 rounded">
                <option value="">Select Security Question</option>
                <option value="pet">What is your pet's name?</option>
                <option value="school">What was your first school?</option>
                <option value="mother">What is your mother's maiden name?</option>
                <option value="city">Where were you born?</option>
                <option value="friend">Your best friend’s name?</option>
                <option value="food">Your favorite food?</option>
              </select>

              <input name="securityAnswer" type="text" placeholder="Security Answer" value={formData.securityAnswer} onChange={handleInputChange} className="w-full border p-2 rounded" />

              <div className="flex items-center space-x-2">
                <input name="agreeToTerms" type="checkbox" checked={formData.agreeToTerms} onChange={handleInputChange} />
                <label className="text-sm">I agree to the Terms and Privacy Policy</label>
              </div>
            </>
          )}

          <button type="submit" className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700">
            {currentView === 'signin' ? 'Login' : 'Create Account'}
          </button>
        </form>

        <p className="mt-4 text-center text-sm">
          {currentView === 'signin' ? "Don't have an account?" : 'Already have an account?'}{' '}
          <button onClick={() => setCurrentView(currentView === 'signin' ? 'signup' : 'signin')} className="text-blue-600 hover:underline">
            {currentView === 'signin' ? 'Sign Up' : 'Login'}
          </button>
        </p>
      </div>
    </div>
  );
};

export default JaiMarketAuthSystem;
