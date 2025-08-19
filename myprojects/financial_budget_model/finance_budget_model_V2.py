import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import warnings
warnings.filterwarnings('ignore')

class AdvancedFinanceBudgetModel:
    def __init__(self, name="Advanced Budget Model", period="Monthly"):
        """
        Advanced Professional Finance Budget Model with Forecasting & Sensitivity Analysis
        
        Args:
            name (str): Name of the budget model
            period (str): Budget period ('Monthly', 'Quarterly', 'Annual')
        """
        self.name = name
        self.period = period
        self.budget_data = {}
        self.actual_data = {}
        self.forecast_data = {}
        self.sensitivity_scenarios = {}
        self.categories = {
            'Revenue': ['Sales', 'Service Income', 'Investment Income', 'Other Revenue'],
            'Operating Expenses': ['Salaries', 'Rent', 'Utilities', 'Marketing', 'Office Supplies', 'Insurance'],
            'Cost of Goods Sold': ['Materials', 'Direct Labor', 'Manufacturing Overhead'],
            'Other Expenses': ['Interest', 'Taxes', 'Depreciation', 'Professional Services']
        }
        self.analysis_results = {}
        self.forecast_results = {}
        self.kpis = {}
        
    def set_budget(self, category, subcategory, amount, months=12):
        """Set budget amounts for specific categories"""
        if category not in self.budget_data:
            self.budget_data[category] = {}
        
        if isinstance(amount, (int, float)):
            self.budget_data[category][subcategory] = [amount] * months
        elif isinstance(amount, list):
            self.budget_data[category][subcategory] = amount[:months]
        
    def set_actual(self, category, subcategory, amount, months=12):
        """Set actual amounts for specific categories"""
        if category not in self.actual_data:
            self.actual_data[category] = {}
            
        if isinstance(amount, (int, float)):
            self.actual_data[category][subcategory] = [amount] * months
        elif isinstance(amount, list):
            self.actual_data[category][subcategory] = amount[:months]
    
    def load_comprehensive_sample_data(self):
        """Load comprehensive sample budget data for demonstration"""
        print("Loading comprehensive sample budget data...")
        
        # Revenue Budget with seasonal trends
        self.set_budget('Revenue', 'Sales', [45000, 47000, 52000, 55000, 58000, 62000,
                                           65000, 63000, 60000, 58000, 70000, 75000])
        self.set_budget('Revenue', 'Service Income', [12000, 13000, 14000, 15000, 16000, 17000,
                                                     18000, 17500, 16500, 16000, 18500, 20000])
        self.set_budget('Revenue', 'Investment Income', [1500, 1600, 1400, 1800, 2000, 2200,
                                                        2100, 1900, 1700, 1800, 2300, 2500])
        self.set_budget('Revenue', 'Other Revenue', [2000, 1500, 2500, 3000, 2800, 3200,
                                                    3500, 3000, 2700, 2900, 4000, 4500])
        
        # Revenue Actuals with realistic variations
        self.set_actual('Revenue', 'Sales', [43000, 48000, 51000, 57000, 59000, 60000,
                                           67000, 64000, 61000, 56000, 72000, 78000])
        self.set_actual('Revenue', 'Service Income', [11500, 13500, 13800, 15200, 16500, 16800,
                                                     18200, 17000, 16200, 15800, 19000, 21000])
        self.set_actual('Revenue', 'Investment Income', [1400, 1550, 1300, 1750, 2100, 2000,
                                                        2200, 1800, 1600, 1900, 2400, 2600])
        self.set_actual('Revenue', 'Other Revenue', [1800, 1600, 2300, 3200, 2900, 3000,
                                                    3700, 2800, 2500, 3100, 4200, 4800])
        
        # Operating Expenses Budget
        self.set_budget('Operating Expenses', 'Salaries', [22000, 22000, 23000, 23000, 24000, 24000,
                                                          25000, 25000, 25000, 26000, 26000, 27000])
        self.set_budget('Operating Expenses', 'Rent', 4500)
        self.set_budget('Operating Expenses', 'Utilities', [1200, 1400, 1100, 1000, 900, 1100,
                                                          1300, 1400, 1200, 1100, 1300, 1500])
        self.set_budget('Operating Expenses', 'Marketing', [2500, 3000, 3500, 4000, 4500, 5000,
                                                          4500, 4000, 3500, 4000, 5500, 6000])
        self.set_budget('Operating Expenses', 'Office Supplies', [600, 700, 650, 800, 750, 900,
                                                                850, 700, 650, 750, 950, 1000])
        self.set_budget('Operating Expenses', 'Insurance', [800, 800, 800, 850, 850, 850,
                                                          900, 900, 900, 950, 950, 950])
        
        # Operating Expenses Actuals
        self.set_actual('Operating Expenses', 'Salaries', [21500, 22200, 23100, 23300, 24200, 23800,
                                                         25200, 25100, 24900, 26200, 26500, 27200])
        self.set_actual('Operating Expenses', 'Rent', 4500)
        self.set_actual('Operating Expenses', 'Utilities', [1250, 1350, 1150, 980, 920, 1050,
                                                          1280, 1420, 1180, 1120, 1280, 1520])
        self.set_actual('Operating Expenses', 'Marketing', [2300, 3200, 3300, 4200, 4300, 4800,
                                                          4200, 3900, 3600, 3800, 5200, 5800])
        self.set_actual('Operating Expenses', 'Office Supplies', [580, 720, 630, 820, 780, 880,
                                                                830, 680, 670, 770, 920, 980])
        self.set_actual('Operating Expenses', 'Insurance', [800, 800, 800, 850, 850, 850,
                                                          900, 900, 900, 950, 950, 950])
        
        # Cost of Goods Sold
        self.set_budget('Cost of Goods Sold', 'Materials', [13500, 14100, 15600, 16500, 17400, 18600,
                                                           19500, 18900, 18000, 17400, 21000, 22500])
        self.set_budget('Cost of Goods Sold', 'Direct Labor', [7000, 7200, 7800, 8000, 8300, 8600,
                                                              8800, 8500, 8200, 8000, 9000, 9500])
        self.set_budget('Cost of Goods Sold', 'Manufacturing Overhead', [2500, 2600, 2800, 2900, 3000, 3100,
                                                                        3200, 3100, 3000, 2900, 3300, 3500])
        
        self.set_actual('Cost of Goods Sold', 'Materials', [13200, 14400, 15300, 17000, 17600, 18200,
                                                           20000, 18600, 17800, 16800, 21500, 23000])
        self.set_actual('Cost of Goods Sold', 'Direct Labor', [6800, 7300, 7600, 8200, 8400, 8400,
                                                              8900, 8300, 8100, 8100, 9200, 9800])
        self.set_actual('Cost of Goods Sold', 'Manufacturing Overhead', [2400, 2650, 2750, 2950, 3050, 3000,
                                                                        3250, 3050, 2950, 2850, 3400, 3600])
        
        # Other Expenses
        self.set_budget('Other Expenses', 'Interest', 500)
        self.set_budget('Other Expenses', 'Taxes', [1000, 1000, 1500, 1500, 2000, 2000,
                                                   2500, 2500, 2000, 2000, 3000, 4000])
        self.set_budget('Other Expenses', 'Depreciation', 1200)
        self.set_budget('Other Expenses', 'Professional Services', [800, 900, 1000, 1200, 1100, 1300,
                                                                   1400, 1200, 1000, 1100, 1500, 1600])
        
        self.set_actual('Other Expenses', 'Interest', 500)
        self.set_actual('Other Expenses', 'Taxes', [950, 1050, 1450, 1600, 1900, 2100,
                                                   2400, 2600, 1950, 2050, 2900, 4100])
        self.set_actual('Other Expenses', 'Depreciation', 1200)
        self.set_actual('Other Expenses', 'Professional Services', [750, 950, 980, 1250, 1050, 1350,
                                                                   1450, 1150, 1020, 1200, 1600, 1700])
        
        print("Comprehensive sample data loaded successfully!")
    
    def create_budget_dataframe(self):
        """Create pandas DataFrame from budget data"""
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        
        budget_rows = []
        actual_rows = []
        
        for category, subcategories in self.budget_data.items():
            for subcategory, values in subcategories.items():
                for i, month in enumerate(months):
                    if i < len(values):
                        budget_rows.append({
                            'Category': category,
                            'Subcategory': subcategory,
                            'Month': month,
                            'Month_Num': i + 1,
                            'Amount': values[i],
                            'Type': 'Budget'
                        })
        
        for category, subcategories in self.actual_data.items():
            for subcategory, values in subcategories.items():
                for i, month in enumerate(months):
                    if i < len(values):
                        actual_rows.append({
                            'Category': category,
                            'Subcategory': subcategory,
                            'Month': month,
                            'Month_Num': i + 1,
                            'Amount': values[i],
                            'Type': 'Actual'
                        })
        
        budget_df = pd.DataFrame(budget_rows)
        actual_df = pd.DataFrame(actual_rows)
        
        return pd.concat([budget_df, actual_df], ignore_index=True)
    
    def calculate_variance_analysis(self):
        """Calculate comprehensive budget vs actual variance analysis"""
        df = self.create_budget_dataframe()
        
        # Pivot to get budget and actual side by side
        pivot_df = df.pivot_table(
            index=['Category', 'Subcategory', 'Month', 'Month_Num'],
            columns='Type',
            values='Amount',
            fill_value=0
        ).reset_index()
        
        # Calculate variance metrics
        pivot_df['Variance'] = pivot_df['Actual'] - pivot_df['Budget']
        pivot_df['Variance %'] = np.where(pivot_df['Budget'] != 0, 
                                         (pivot_df['Variance'] / pivot_df['Budget'] * 100), 0).round(2)
        pivot_df['Abs Variance %'] = abs(pivot_df['Variance %'])
        pivot_df['Favorable'] = pivot_df.apply(
            lambda row: 'Favorable' if (
                (row['Category'] == 'Revenue' and row['Variance'] > 0) or
                (row['Category'] != 'Revenue' and row['Variance'] < 0)
            ) else 'Unfavorable', axis=1
        )
        
        # Add performance categories
        pivot_df['Performance'] = pd.cut(pivot_df['Abs Variance %'], 
                                       bins=[0, 5, 15, 100], 
                                       labels=['Excellent', 'Good', 'Poor'])
        
        self.variance_analysis = pivot_df
        return pivot_df
    
    def generate_forecasting_models(self, forecast_months=6):
        """Generate forecasting models using multiple methods"""
        df = self.calculate_variance_analysis()
        
        # Prepare forecast results
        self.forecast_results = {}
        
        for category in df['Category'].unique():
            self.forecast_results[category] = {}
            category_data = df[df['Category'] == category]
            
            for subcategory in category_data['Subcategory'].unique():
                subcat_data = category_data[category_data['Subcategory'] == subcategory]
                actual_values = subcat_data['Actual'].values
                months = subcat_data['Month_Num'].values
                
                # Method 1: Linear Regression
                lr_model = LinearRegression()
                lr_model.fit(months.reshape(-1, 1), actual_values)
                future_months = np.arange(13, 13 + forecast_months)
                linear_forecast = lr_model.predict(future_months.reshape(-1, 1))
                
                # Method 2: Moving Average (3-month)
                ma_forecast = []
                for i in range(forecast_months):
                    if i == 0:
                        ma_value = np.mean(actual_values[-3:])
                    else:
                        recent_values = list(actual_values[-3+i:]) + ma_forecast[:i]
                        ma_value = np.mean(recent_values[-3:])
                    ma_forecast.append(ma_value)
                
                # Method 3: Seasonal Trend
                seasonal_avg = np.mean([actual_values[i::12] for i in range(min(12, len(actual_values)))], axis=1)
                growth_rate = (actual_values[-1] - actual_values[0]) / len(actual_values)
                seasonal_forecast = []
                for i in range(forecast_months):
                    month_idx = (12 + i) % 12
                    if month_idx < len(seasonal_avg):
                        base_value = seasonal_avg[month_idx]
                        trend_adjustment = growth_rate * (12 + i + 1)
                        seasonal_forecast.append(max(0, base_value + trend_adjustment))
                    else:
                        seasonal_forecast.append(actual_values[-1] * (1 + growth_rate))
                
                # Method 4: Exponential Smoothing
                alpha = 0.3
                exp_forecast = [actual_values[-1]]
                for i in range(1, forecast_months):
                    exp_value = alpha * exp_forecast[-1] + (1 - alpha) * np.mean(actual_values[-3:])
                    exp_forecast.append(exp_value)
                
                # Ensemble forecast (average of methods)
                ensemble_forecast = np.mean([linear_forecast, ma_forecast, seasonal_forecast, exp_forecast], axis=0)
                
                self.forecast_results[category][subcategory] = {
                    'linear': linear_forecast,
                    'moving_average': ma_forecast,
                    'seasonal': seasonal_forecast,
                    'exponential': exp_forecast,
                    'ensemble': ensemble_forecast,
                    'confidence_interval': {
                        'lower': ensemble_forecast * 0.85,
                        'upper': ensemble_forecast * 1.15
                    }
                }
        
        return self.forecast_results
    
    def sensitivity_analysis(self, scenarios=None):
        """Perform sensitivity analysis with multiple scenarios"""
        if scenarios is None:
            scenarios = {
                'Optimistic': {'revenue_change': 0.15, 'expense_change': -0.05},
                'Pessimistic': {'revenue_change': -0.10, 'expense_change': 0.08},
                'High Inflation': {'revenue_change': 0.05, 'expense_change': 0.12},
                'Recession': {'revenue_change': -0.25, 'expense_change': 0.03},
                'Best Case': {'revenue_change': 0.25, 'expense_change': -0.10}
            }
        
        base_analysis = self.analysis_results['key_metrics']
        self.sensitivity_scenarios = {}
        
        for scenario_name, changes in scenarios.items():
            # Calculate adjusted values
            adj_revenue = base_analysis['Total Revenue (Actual)'] * (1 + changes['revenue_change'])
            adj_expenses = base_analysis['Total Expenses (Actual)'] * (1 + changes['expense_change'])
            adj_net_income = adj_revenue - adj_expenses
            
            self.sensitivity_scenarios[scenario_name] = {
                'Revenue': adj_revenue,
                'Expenses': adj_expenses,
                'Net Income': adj_net_income,
                'Revenue Change %': changes['revenue_change'] * 100,
                'Expense Change %': changes['expense_change'] * 100,
                'Net Income Change $': adj_net_income - base_analysis['Net Income (Actual)'],
                'Net Income Change %': ((adj_net_income - base_analysis['Net Income (Actual)']) / 
                                      abs(base_analysis['Net Income (Actual)']) * 100) if base_analysis['Net Income (Actual)'] != 0 else 0
            }
        
        return self.sensitivity_scenarios
    
    def calculate_advanced_kpis(self):
        """Calculate advanced Key Performance Indicators"""
        analysis = self.analysis_results['key_metrics']
        variance_df = self.variance_analysis
        
        # Financial KPIs
        gross_profit = analysis['Total Revenue (Actual)'] - variance_df[
            variance_df['Category'] == 'Cost of Goods Sold']['Actual'].sum()
        gross_margin = (gross_profit / analysis['Total Revenue (Actual)']) * 100 if analysis['Total Revenue (Actual)'] != 0 else 0
        
        operating_expenses = variance_df[variance_df['Category'] == 'Operating Expenses']['Actual'].sum()
        operating_income = gross_profit - operating_expenses
        operating_margin = (operating_income / analysis['Total Revenue (Actual)']) * 100 if analysis['Total Revenue (Actual)'] != 0 else 0
        
        net_margin = (analysis['Net Income (Actual)'] / analysis['Total Revenue (Actual)']) * 100 if analysis['Total Revenue (Actual)'] != 0 else 0
        
        # Budget Performance KPIs
        total_budget_accuracy = (1 - abs(analysis['Net Income Variance']) / abs(analysis['Net Income (Budget)'])) * 100 if analysis['Net Income (Budget)'] != 0 else 0
        revenue_forecast_accuracy = (1 - abs(analysis['Revenue Variance']) / analysis['Total Revenue (Budget)']) * 100 if analysis['Total Revenue (Budget)'] != 0 else 0
        expense_forecast_accuracy = (1 - abs(analysis['Expense Variance']) / analysis['Total Expenses (Budget)']) * 100 if analysis['Total Expenses (Budget)'] != 0 else 0
        
        # Variability KPIs
        monthly_revenue = variance_df[variance_df['Category'] == 'Revenue'].groupby('Month')['Actual'].sum()
        revenue_volatility = (monthly_revenue.std() / monthly_revenue.mean()) * 100 if monthly_revenue.mean() != 0 else 0
        
        self.kpis = {
            'Financial Performance': {
                'Gross Profit': gross_profit,
                'Gross Margin %': gross_margin,
                'Operating Income': operating_income,
                'Operating Margin %': operating_margin,
                'Net Margin %': net_margin
            },
            'Budget Performance': {
                'Overall Budget Accuracy %': total_budget_accuracy,
                'Revenue Forecast Accuracy %': revenue_forecast_accuracy,
                'Expense Forecast Accuracy %': expense_forecast_accuracy
            },
            'Risk Metrics': {
                'Revenue Volatility %': revenue_volatility,
                'Break-even Revenue': operating_expenses + variance_df[variance_df['Category'] == 'Cost of Goods Sold']['Actual'].sum()
            }
        }
        
        return self.kpis
    
    def generate_comprehensive_analysis(self):
        """Generate comprehensive financial analysis"""
        df = self.calculate_variance_analysis()
        
        # Monthly summary
        monthly_summary = df.groupby(['Month', 'Category']).agg({
            'Budget': 'sum',
            'Actual': 'sum',
            'Variance': 'sum'
        }).reset_index()
        
        # Annual summary by category
        annual_summary = df.groupby('Category').agg({
            'Budget': 'sum',
            'Actual': 'sum',
            'Variance': 'sum'
        }).round(2)
        annual_summary['Variance %'] = (annual_summary['Variance'] / annual_summary['Budget'] * 100).round(2)
        
        # Calculate key metrics
        total_revenue_budget = annual_summary.loc['Revenue', 'Budget']
        total_revenue_actual = annual_summary.loc['Revenue', 'Actual']
        
        total_expenses_budget = annual_summary.loc[annual_summary.index != 'Revenue', 'Budget'].sum()
        total_expenses_actual = annual_summary.loc[annual_summary.index != 'Revenue', 'Actual'].sum()
        
        net_income_budget = total_revenue_budget - total_expenses_budget
        net_income_actual = total_revenue_actual - total_expenses_actual
        
        self.analysis_results = {
            'monthly_summary': monthly_summary,
            'annual_summary': annual_summary,
            'key_metrics': {
                'Total Revenue (Budget)': total_revenue_budget,
                'Total Revenue (Actual)': total_revenue_actual,
                'Total Expenses (Budget)': total_expenses_budget,
                'Total Expenses (Actual)': total_expenses_actual,
                'Net Income (Budget)': net_income_budget,
                'Net Income (Actual)': net_income_actual,
                'Revenue Variance': total_revenue_actual - total_revenue_budget,
                'Expense Variance': total_expenses_actual - total_expenses_budget,
                'Net Income Variance': net_income_actual - net_income_budget
            }
        }
        
        # Generate forecasting
        self.generate_forecasting_models()
        
        # Perform sensitivity analysis
        self.sensitivity_analysis()
        
        # Calculate KPIs
        self.calculate_advanced_kpis()
        
        return self.analysis_results
    
    def create_comprehensive_visualizations(self):
        """Create comprehensive financial visualizations"""
        if not hasattr(self, 'variance_analysis'):
            self.calculate_variance_analysis()
        
        # Set style for professional look
        plt.style.use('default')
        sns.set_palette("husl")
        
        # Create a large figure with multiple subplots
        fig = plt.figure(figsize=(20, 16))
        gs = fig.add_gridspec(4, 3, height_ratios=[1, 1, 1, 1], width_ratios=[1, 1, 1])
        
        fig.suptitle(f'{self.name} - Comprehensive Financial Analysis Dashboard', 
                    fontsize=18, fontweight='bold', y=0.98)
        
        # 1. Monthly Revenue & Expense Trend
        ax1 = fig.add_subplot(gs[0, :2])
        monthly_data = self.variance_analysis.groupby(['Month', 'Category'])[['Budget', 'Actual']].sum().reset_index()
        revenue_data = monthly_data[monthly_data['Category'] == 'Revenue'].set_index('Month')
        expense_data = monthly_data[monthly_data['Category'] != 'Revenue'].groupby('Month')[['Budget', 'Actual']].sum()
        
        months_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        revenue_data = revenue_data.reindex(months_order)
        expense_data = expense_data.reindex(months_order)
        
        ax1.plot(months_order, revenue_data['Actual'], 'o-', label='Revenue (Actual)', linewidth=2, markersize=6)
        ax1.plot(months_order, revenue_data['Budget'], 's--', label='Revenue (Budget)', linewidth=2, markersize=6)
        ax1.plot(months_order, expense_data['Actual'], '^-', label='Expenses (Actual)', linewidth=2, markersize=6)
        ax1.plot(months_order, expense_data['Budget'], 'd--', label='Expenses (Budget)', linewidth=2, markersize=6)
        
        ax1.set_title('Monthly Revenue & Expense Trends', fontweight='bold', fontsize=12)
        ax1.set_ylabel('Amount ($)', fontweight='bold')
        ax1.legend(loc='upper left')
        ax1.grid(True, alpha=0.3)
        ax1.tick_params(axis='x', rotation=45)
        
        # 2. Waterfall Chart for Net Income
        ax2 = fig.add_subplot(gs[0, 2])
        metrics = self.analysis_results['key_metrics']
        categories = ['Revenue\n(Actual)', 'COGS', 'Operating\nExpenses', 'Other\nExpenses', 'Net\nIncome']
        
        cogs_actual = -self.variance_analysis[self.variance_analysis['Category'] == 'Cost of Goods Sold']['Actual'].sum()
        opex_actual = -self.variance_analysis[self.variance_analysis['Category'] == 'Operating Expenses']['Actual'].sum()
        other_actual = -self.variance_analysis[self.variance_analysis['Category'] == 'Other Expenses']['Actual'].sum()
        
        values = [metrics['Total Revenue (Actual)'], cogs_actual, opex_actual, other_actual, metrics['Net Income (Actual)']]
        colors = ['green', 'red', 'red', 'red', 'blue' if metrics['Net Income (Actual)'] > 0 else 'red']
        
        bars = ax2.bar(categories, values, color=colors, alpha=0.7)
        ax2.set_title('Income Statement Waterfall', fontweight='bold', fontsize=12)
        ax2.set_ylabel('Amount ($)', fontweight='bold')
        ax2.tick_params(axis='x', rotation=45)
        ax2.axhline(y=0, color='black', linestyle='-', alpha=0.3)
        
        # Add value labels
        for bar, value in zip(bars, values):
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height + (abs(height) * 0.01),
                    f'${value:,.0f}', ha='center', va='bottom' if height > 0 else 'top', fontsize=9)
        
        # 3. Variance Heatmap
        ax3 = fig.add_subplot(gs[1, :2])
        variance_pivot = self.variance_analysis.pivot_table(
            index='Subcategory', columns='Month', values='Variance %', fill_value=0
        )
        variance_pivot = variance_pivot.reindex(columns=months_order, fill_value=0)
        
        sns.heatmap(variance_pivot, annot=True, fmt='.1f', cmap='RdYlGn', center=0, 
                   ax=ax3, cbar_kws={'label': 'Variance %'})
        ax3.set_title('Budget Variance Heatmap (%)', fontweight='bold', fontsize=12)
        ax3.set_xlabel('Month', fontweight='bold')
        ax3.set_ylabel('Subcategory', fontweight='bold')
        
        # 4. Performance Distribution
        ax4 = fig.add_subplot(gs[1, 2])
        performance_counts = self.variance_analysis['Performance'].value_counts()
        colors_perf = {'Excellent': 'green', 'Good': 'orange', 'Poor': 'red'}
        wedges, texts, autotexts = ax4.pie(performance_counts.values, 
                                          labels=performance_counts.index,
                                          autopct='%1.1f%%',
                                          colors=[colors_perf[x] for x in performance_counts.index],
                                          startangle=90)
        ax4.set_title('Budget Performance Distribution', fontweight='bold', fontsize=12)
        
        # 5. Forecasting Chart
        ax5 = fig.add_subplot(gs[2, :2])
        if hasattr(self, 'forecast_results') and 'Revenue' in self.forecast_results:
            # Show forecast for main revenue stream
            main_revenue = list(self.forecast_results['Revenue'].keys())[0]
            forecast_data = self.forecast_results['Revenue'][main_revenue]['ensemble']
            
            # Historical data
            historical = self.variance_analysis[
                (self.variance_analysis['Category'] == 'Revenue') & 
                (self.variance_analysis['Subcategory'] == main_revenue)
            ]['Actual'].values
            
            # Combine historical and forecast
            all_months = list(range(1, 13)) + list(range(13, 19))  # 12 historical + 6 forecast
            historical_extended = list(historical) + [None] * 6
            forecast_extended = [None] * 12 + list(forecast_data)
            
            ax5.plot(range(1, 13), historical, 'o-', label='Historical Actual', linewidth=2, markersize=6)
            ax5.plot(range(13, 19), forecast_data, 's