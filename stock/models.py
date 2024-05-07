from django.db import models


# Create your models here.


class StockInfo(models.Model):
    """股票信息"""
    STOCK_TYPE = [
        ('A', 'A股'),
        ('B', 'B股'),
        ('H', 'H股')
    ]
    stock_code = models.CharField(max_length=10, unique=True, primary_key=True, verbose_name='股票代码')
    stock_name = models.CharField(max_length=100, verbose_name='股票名称')
    company_name = models.CharField(max_length=100, verbose_name='公司名称')
    stock_type = models.CharField(max_length=1, choices=STOCK_TYPE, verbose_name='股票类型')
    market = models.CharField(max_length=10, verbose_name='所属市场')
    industry = models.CharField(max_length=100, verbose_name='所属行业')
    start_date = models.DateField(verbose_name='成立日期')
    list_date = models.DateField(verbose_name='上市日期')
    address = models.CharField(max_length=100, verbose_name='公司地址')
    postcode = models.CharField(max_length=6, verbose_name='公司邮编')

    class Meta:
        db_table = 'stock_info'
        verbose_name = '股票信息'
        verbose_name_plural = verbose_name


class StockDailyPrice(models.Model):
    """股票日线价格"""
    stock_code = models.CharField(max_length=10, verbose_name='股票代码')
    stock_name = models.CharField(max_length=100, verbose_name='股票名称')
    date = models.DateField(verbose_name='日期')
    open_price = models.FloatField(verbose_name='开盘价')
    high_price = models.FloatField(verbose_name='最高价')
    low_price = models.FloatField(verbose_name='最低价')
    close_price = models.FloatField(verbose_name='收盘价')
    volume = models.BigIntegerField(verbose_name='成交量')
    amount = models.FloatField(verbose_name='成交额')
    p_change = models.FloatField(verbose_name='涨跌幅')

    class Meta:
        db_table = 'stock_daily_price'
        verbose_name = '股票日线'
        verbose_name_plural = verbose_name


class StockDailyInfo(models.Model):
    """股票日度信息"""
    stock_code = models.CharField(max_length=10, verbose_name='股票代码')
    stock_name = models.CharField(max_length=100, verbose_name='股票名称')
    date = models.DateField(verbose_name='日期')
    market_value = models.FloatField(verbose_name='总市值')
    circulation_value = models.FloatField(verbose_name='流通市值')
    pe_ratio = models.FloatField(verbose_name='市盈率')
    pb_ratio = models.FloatField(verbose_name='市净率')
    dividend_yield = models.FloatField(verbose_name='股息率')

    class Meta:
        db_table = 'stock_daily_info'
        verbose_name = '股票日度信息'
        verbose_name_plural = verbose_name


class StockBalanceSheet(models.Model):
    """股票资产负债表"""
    stock_code = models.CharField(max_length=10, verbose_name='股票代码')
    stock_name = models.CharField(max_length=100, verbose_name='股票名称')
    date = models.DateField(verbose_name='日期')
    assets_currency = models.FloatField(verbose_name='资产-货币资金')
    assets_receives = models.FloatField(verbose_name='资产-应收账款')
    assets_inventory = models.FloatField(verbose_name='资产-存货')
    total_assets = models.FloatField(verbose_name='总资产')
    total_assets_tb = models.FloatField(verbose_name='总资产-同比')
    liabilities_payable = models.FloatField(verbose_name='负债-应付账款')
    liabilities = models.FloatField(verbose_name='总负债')
    liabilities_prepayment = models.FloatField(verbose_name='负债-预收款')
    liabilities_tb = models.FloatField(verbose_name='总负债-同比')
    liabilities_assets = models.FloatField(verbose_name='资产负债率')
    current_liabilities = models.FloatField(verbose_name='流动负债')
    shareholder_equity = models.FloatField(verbose_name='股东权益')

    class Meta:
        db_table = 'stock_balance_sheet'
        verbose_name = '股票资产负债表'
        verbose_name_plural = verbose_name


class StockCashFlow(models.Model):
    """股票现金流量表"""
    stock_code = models.CharField(max_length=10, verbose_name='股票代码')
    stock_name = models.CharField(max_length=100, verbose_name='股票名称')
    date = models.DateField(verbose_name='日期')
    operating_cash_flow = models.FloatField(verbose_name='经营活动产生的现金流量')
    investment_cash_flow = models.FloatField(verbose_name='投资活动产生的现金流量')
    financing_cash_flow = models.FloatField(verbose_name='筹资活动产生的现金流量')
    cash_flow_from_operations = models.FloatField(verbose_name='经营活动产生的现金流量净额')
    cash_flow_from_investment = models.FloatField(verbose_name='投资活动产生的现金流量净额')
    cash_flow_from_financing = models.FloatField(verbose_name='筹资活动产生的现金流量净额')

    class Meta:
        db_table = 'stock_cash_flow'
        verbose_name = '股票现金流量表'
        verbose_name_plural = verbose_name


class StockIncomeStatement(models.Model):
    """股票利润表"""
    stock_code = models.CharField(max_length=10, verbose_name='股票代码')
    stock_name = models.CharField(max_length=100, verbose_name='股票名称')
    date = models.DateField(verbose_name='日期')
    net_profit = models.FloatField(verbose_name='净利润')
    net_profit_tb = models.FloatField(verbose_name='净利润-同比')
    revenue = models.FloatField(verbose_name='营业收入')
    revenue_tb = models.FloatField(verbose_name='营业收入-同比')
    operating_expenses = models.FloatField(verbose_name='营业支出')
    sale_expenses = models.FloatField(verbose_name='销售费用')
    manage_expenses = models.FloatField(verbose_name='管理费用')
    finance_expenses = models.FloatField(verbose_name='财务费用')
    operating_profit = models.FloatField(verbose_name='营业利润')

    class Meta:
        db_table = 'stock_income_statement'
        verbose_name = '股票利润表'
        verbose_name_plural = verbose_name
