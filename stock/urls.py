from django.urls import path


from . import views

urlpatterns = [

    path('info-list/', views.StockInfoListView.as_view(), name='stock_info_list'),
    path('info/', views.StockInfoView.as_view(), name='stock_info_detail'),
    path('daily-list/', views.StockDailyInfoListView.as_view(), name='stock_daily_list'),
    path('daily/', views.StockDailyInfoView.as_view(), name='stock_daily_detail'),
    path('price-list/', views.StockDailyPriceListView.as_view(), name='stock_daily_price_list'),
    path('price/', views.StockDailyPriceView.as_view(), name='stock_daily_price_detail'),
    path('bs-list', views.StockBalanceSheetListView.as_view(), name='stock_balance_sheet_list'),
    path('bs/', views.StockBalanceSheetView.as_view(), name='stock_balance_sheet_detail'),
    path('cf-list', views.StockCashFlowListView.as_view(), name='stock_cash_flow_list'),
    path('cf/', views.StockCashFlowView.as_view(), name='stock_cash_flow_detail'),
    path('is-list', views.StockIncomeStatementListView.as_view(), name='stock_income_statement_list'),
    path('is/', views.StockIncomeStatementView.as_view(), name='stock_income_statement_detail'),

]