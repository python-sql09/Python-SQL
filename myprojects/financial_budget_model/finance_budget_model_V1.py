import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

class FinanceBudgetModel:
    def __init__(self, name="Budget Model", period="Monthly"):
        """
        Professional Finance Budget Model
        
        Args:
            name (str): Name of the budget model
            period (str): Budget period ('Monthly', 'Quarterly', 'Annual')
        """
        self.name = name
        self.period = period
        self.budget_data = {}
        self.actual_data = {}
        self.categories = {
            'Revenue': ['Sales', 'Service Income', 'Investment Income', 'Other Revenue'],
            'Operating Expenses': ['Salaries', 'Rent', 'Utilities', 'Marketing', 'Office Supplies'],
            'Cost of Goods Sold': ['Materials', 'Direct Labor', 'Manufacturing Overhead'],
            'Other Expenses': ['Interest', 'Taxes', 'Depreciation', 'Insurance']
        }
        self.analysis_results = {}
        
    def set_budget(self, category, subcategory, amount, months=12):
        """Set budget amounts for specific categories"""
        if category not in self.budget_data:
            self.budget_data[category] = {}
        
        if isinstance(amount, (int, float)):
            # Single amount for all periods
            self.budget_data[category][subcategory] = [amount] * months
        elif isinstance(amount, list):
            # Different amounts per period
            self.budget_data[category][subcategory] = amount[:months]
        
    def set_actual(self, category, subcategory, amount, months=12):
        """Set actual amounts for specific categories"""
        if category not in self.actual_data:
            self.actual_data[category] = {}
            
        if isinstance(amount, (int, float)):
            self.actual_data[category][subcategory] = [amount] * months
        elif isinstance(amount, list):
            self.actual_data[category][subcategory] = amount[:months]
    
    def load_sample_data(self):
        """Load sample budget data for demonstration"""
        print("Loading sample budget data...")
        
        # Revenue Budget
        self.set_budget('Revenue', 'Sales', [50000, 52000, 48000, 55000, 58000, 60000,
                                           62000, 59000, 61000, 63000, 65000, 70000])
        self.set_budget('Revenue', 'Service Income', 15000)
        self.set_budget('Revenue', 'Investment Income', 2000)
        
        # Revenue Actuals
        self.set_actual('Revenue', 'Sales', [48000, 51000, 49000, 54000, 57000, 58000,
                                           61000, 60000, 62000, 64000, 66000, 72000])
        self.set_actual('Revenue', 'Service Income', [14500, 15200, 14800, 15500, 15800, 16000,
                                                     15200, 15600, 15900, 16200, 16500, 17000])
        self.set_actual('Revenue', 'Investment Income', 1800)
        
        # Operating Expenses Budget
        self.set_budget('Operating Expenses', 'Salaries', 25000)
        self.set_budget('Operating Expenses', 'Rent', 5000)
        self.set_budget('Operating Expenses', 'Utilities', 1500)
        self.set_budget('Operating Expenses', 'Marketing', [3000, 3500, 2500, 4000, 4500, 5000,
                                                          4000, 3500, 4200, 4800, 5500, 6000])
        self.set_budget('Operating Expenses', 'Office Supplies', 800)
        
        # Operating Expenses Actuals
        self.set_actual('Operating Expenses', 'Salaries', [24500, 25200, 25000, 25800, 26000, 25500,
                                                         25800, 26200, 25900, 26500, 27000, 27500])
        self.set_actual('Operating Expenses', 'Rent', 5000)
        self.set_actual('Operating Expenses', 'Utilities', [1450, 1520, 1480, 1550, 1600, 1750,
                                                          1800, 1650, 1580, 1620, 1680, 1720])
        self.set_actual('Operating Expenses', 'Marketing', [2800, 3200, 2600, 3800, 4200, 4800,
                                                          3900, 3600, 4100, 4900, 5200, 5800])
        self.set_actual('Operating Expenses', 'Office Supplies', [750, 820, 780, 850, 900, 880,
                                                                840, 790, 810, 870, 920, 950])
        
        # Cost of Goods Sold
        self.set_budget('Cost of Goods Sold', 'Materials', [15000, 15600, 14400, 16500, 17400, 18000,
                                                           18600, 17700, 18300, 18900, 19500, 21000])
        self.set_budget('Cost of Goods Sold', 'Direct Labor', 8000)
        self.set_budget('Cost of Goods Sold', 'Manufacturing Overhead', 3000)
        
        self.set_actual('Cost of Goods Sold', 'Materials', [14800, 15200, 14600, 16200, 17100, 17800,
                                                           18400, 18000, 18500, 19200, 19800, 21500])
        self.set_actual('Cost of Goods Sold', 'Direct Labor', [7800, 8100, 7900, 8200, 8300, 8000,
                                                              8150, 8250, 8100, 8400, 8500, 8600])
        self.set_actual('Cost of Goods Sold', 'Manufacturing Overhead', 2950)
        
        print("Sample data loaded successfully!")
    
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
                            'Amount': values[i],
                            'Type': 'Actual'
                        })
        
        budget_df = pd.DataFrame(budget_rows)
        actual_df = pd.DataFrame(actual_rows)
        
        return pd.concat([budget_df, actual_df], ignore_index=True)
    
    def calculate_variance_analysis(self):
        """Calculate budget vs actual variance analysis"""
        df = self.create_budget_dataframe()
        
        # Pivot to get budget and actual side by side
        pivot_df = df.pivot_table(
            index=['Category', 'Subcategory', 'Month'],
            columns='Type',
            values='Amount',
            fill_value=0
        ).reset_index()
        
        # Calculate variance
        pivot_df['Variance'] = pivot_df['Actual'] - pivot_df['Budget']
        pivot_df['Variance %'] = (pivot_df['Variance'] / pivot_df['Budget'] * 100).round(2)
        pivot_df['Favorable'] = pivot_df.apply(
            lambda row: 'Favorable' if (
                (row['Category'] == 'Revenue' and row['Variance'] > 0) or
                (row['Category'] != 'Revenue' and row['Variance'] < 0)
            ) else 'Unfavorable', axis=1
        )
        
        self.variance_analysis = pivot_df
        return pivot_df
    
    def generate_financial_summary(self):
        """Generate comprehensive financial summary"""
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
        
        return self.analysis_results
    
    def create_visualizations(self):
        """Create professional financial visualizations"""
        if not hasattr(self, 'variance_analysis'):
            self.calculate_variance_analysis()
        
        # Set style for professional look
        plt.style.use('seaborn-v0_8')
        sns.set_palette("husl")
        
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle(f'{self.name} - Financial Analysis Dashboard', fontsize=16, fontweight='bold')
        
        # 1. Monthly Revenue Trend
        revenue_data = self.variance_analysis[self.variance_analysis['Category'] == 'Revenue']
        monthly_revenue = revenue_data.groupby('Month')[['Budget', 'Actual']].sum()
        monthly_revenue.index = pd.Categorical(monthly_revenue.index, 
                                             categories=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                                             ordered=True)
        monthly_revenue = monthly_revenue.sort_index()
        
        monthly_revenue.plot(kind='line', ax=axes[0,0], marker='o', linewidth=2)
        axes[0,0].set_title('Monthly Revenue: Budget vs Actual', fontweight='bold')
        axes[0,0].set_ylabel('Amount ($)')
        axes[0,0].grid(True, alpha=0.3)
        axes[0,0].legend()
        
        # 2. Expense Breakdown
        expense_data = self.variance_analysis[self.variance_analysis['Category'] != 'Revenue']
        expense_summary = expense_data.groupby('Category')['Actual'].sum()
        
        colors = plt.cm.Set3(np.linspace(0, 1, len(expense_summary)))
        wedges, texts, autotexts = axes[0,1].pie(expense_summary.values, 
                                                labels=expense_summary.index,
                                                autopct='%1.1f%%',
                                                colors=colors,
                                                startangle=90)
        axes[0,1].set_title('Expense Distribution (Actual)', fontweight='bold')
        
        # 3. Variance Analysis by Category
        category_variance = self.variance_analysis.groupby('Category')['Variance'].sum()
        colors = ['green' if x > 0 else 'red' for x in category_variance.values]
        
        bars = axes[1,0].bar(category_variance.index, category_variance.values, color=colors, alpha=0.7)
        axes[1,0].set_title('Budget Variance by Category', fontweight='bold')
        axes[1,0].set_ylabel('Variance ($)')
        axes[1,0].tick_params(axis='x', rotation=45)
        axes[1,0].axhline(y=0, color='black', linestyle='-', alpha=0.3)
        axes[1,0].grid(True, alpha=0.3)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            axes[1,0].text(bar.get_x() + bar.get_width()/2., height,
                          f'${height:,.0f}', ha='center', va='bottom' if height > 0 else 'top')
        
        # 4. Monthly Cash Flow
        cash_flow_data = self.variance_analysis.groupby('Month').apply(
            lambda x: x[x['Category'] == 'Revenue']['Actual'].sum() - 
                     x[x['Category'] != 'Revenue']['Actual'].sum()
        )
        cash_flow_data.index = pd.Categorical(cash_flow_data.index,
                                            categories=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                                      'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                                            ordered=True)
        cash_flow_data = cash_flow_data.sort_index()
        
        colors = ['green' if x > 0 else 'red' for x in cash_flow_data.values]
        bars = axes[1,1].bar(cash_flow_data.index, cash_flow_data.values, color=colors, alpha=0.7)
        axes[1,1].set_title('Monthly Net Cash Flow', fontweight='bold')
        axes[1,1].set_ylabel('Net Cash Flow ($)')
        axes[1,1].axhline(y=0, color='black', linestyle='-', alpha=0.3)
        axes[1,1].grid(True, alpha=0.3)
        
        # Add value labels
        for bar in bars:
            height = bar.get_height()
            axes[1,1].text(bar.get_x() + bar.get_width()/2., height,
                          f'${height:,.0f}', ha='center', va='bottom' if height > 0 else 'top',
                          fontsize=8)
        
        plt.tight_layout()
        plt.show()
    
    def export_to_excel(self, filename=None):
        """Export budget model to Excel file"""
        if filename is None:
            filename = f"{self.name.replace(' ', '_')}_Budget_Model_{datetime.now().strftime('%Y%m%d')}.xlsx"
        
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            # Summary sheet
            summary_df = pd.DataFrame.from_dict(self.analysis_results['key_metrics'], 
                                              orient='index', columns=['Amount'])
            summary_df.to_excel(writer, sheet_name='Summary')
            
            # Detailed variance analysis
            self.variance_analysis.to_excel(writer, sheet_name='Variance Analysis', index=False)
            
            # Monthly summary
            self.analysis_results['monthly_summary'].to_excel(writer, sheet_name='Monthly Summary', index=False)
            
            # Annual summary
            self.analysis_results['annual_summary'].to_excel(writer, sheet_name='Annual Summary')
            
        print(f"Budget model exported to: {filename}")
        return filename
    
    def print_summary_report(self):
        """Print comprehensive summary report"""
        print("=" * 80)
        print(f"FINANCIAL BUDGET ANALYSIS REPORT - {self.name}")
        print("=" * 80)
        print(f"Report Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Budget Period: {self.period}")
        print()
        
        # Key Metrics
        print("KEY FINANCIAL METRICS")
        print("-" * 40)
        metrics = self.analysis_results['key_metrics']
        for metric, value in metrics.items():
            print(f"{metric:<30}: ${value:>12,.2f}")
        
        print()
        
        # Performance Analysis
        revenue_variance_pct = (metrics['Revenue Variance'] / metrics['Total Revenue (Budget)'] * 100)
        expense_variance_pct = (metrics['Expense Variance'] / metrics['Total Expenses (Budget)'] * 100)
        
        print("PERFORMANCE ANALYSIS")
        print("-" * 40)
        print(f"Revenue Performance    : {revenue_variance_pct:>6.1f}% {'(Favorable)' if revenue_variance_pct > 0 else '(Unfavorable)'}")
        print(f"Expense Performance    : {expense_variance_pct:>6.1f}% {'(Favorable)' if expense_variance_pct < 0 else '(Unfavorable)'}")
        print(f"Overall Net Performance: ${metrics['Net Income Variance']:>10,.2f}")
        
        print()
        
        # Category Performance
        print("CATEGORY PERFORMANCE SUMMARY")
        print("-" * 80)
        annual_summary = self.analysis_results['annual_summary']
        print(f"{'Category':<20} {'Budget':>12} {'Actual':>12} {'Variance':>12} {'Variance %':>12}")
        print("-" * 80)
        for category in annual_summary.index:
            row = annual_summary.loc[category]
            print(f"{category:<20} ${row['Budget']:>11,.0f} ${row['Actual']:>11,.0f} ${row['Variance']:>11,.0f} {row['Variance %']:>10.1f}%")
        
        print("=" * 80)

# Example usage and demonstration
def main():
    """Main function to demonstrate the budget model"""
    # Create budget model instance
    budget_model = FinanceBudgetModel("Company XYZ Annual Budget", "Monthly")
    
    # Load sample data
    budget_model.load_sample_data()
    
    # Generate analysis
    budget_model.generate_financial_summary()
    
    # Print summary report
    budget_model.print_summary_report()
    
    # Create visualizations
    print("\nGenerating visualizations...")
    budget_model.create_visualizations()
    
    # Export to Excel
    print("\nExporting to Excel...")
    excel_file = budget_model.export_to_excel()
    
    print(f"\nBudget model analysis complete!")
    print(f"Excel file saved as: {excel_file}")
    
    return budget_model

if __name__ == "__main__":
    model = main()
