from rest_framework import serializers
from .models import StockInfo, StockDailyInfo, StockDailyPrice, StockBalanceSheet, StockIncomeStatement, StockCashFlow


class StockInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockInfo
        fields = '__all__'


class StockDailyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockDailyInfo
        fields = '__all__'


class StockDailyPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockDailyPrice
        fields = '__all__'


class StockBalanceSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockBalanceSheet
        fields = '__all__'


class StockIncomeStatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockIncomeStatement
        fields = '__all__'


class StockCashFlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockCashFlow
        fields = '__all__'
