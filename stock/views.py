from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import StockInfoSerializer, StockDailyInfoSerializer, StockDailyPriceSerializer, \
    StockBalanceSheetSerializer, StockIncomeStatementSerializer, StockCashFlowSerializer
from .models import StockInfo, StockDailyInfo, StockDailyPrice, StockBalanceSheet, StockIncomeStatement, StockCashFlow


# Create your views here.
class StockInfoListView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        stock_info = StockInfo.objects.all()
        serializer = StockInfoSerializer(stock_info, many=True)
        return Response(serializer.data)


class StockInfoView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, stock_code):
        stock_info = StockInfo.objects.filter(stock_code=stock_code).first()

        if stock_info:
            serializer = StockInfoSerializer(stock_info)
            return Response(serializer.data)

        return Response({'error': 'Stock information not found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = StockInfoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StockDailyInfoListView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        stock_daily_info = StockDailyInfo.objects.all()
        serializer = StockDailyInfoSerializer(stock_daily_info, many=True)
        return Response(serializer.data)


class StockDailyInfoView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, stock_code):
        stock_daily_info = StockDailyInfo.objects.filter(stock_code=stock_code).first()

        if stock_daily_info:
            serializer = StockDailyInfoSerializer(stock_daily_info)
            return Response(serializer.data)

        return Response({'error': 'Stock daily information not found'}, status=status.HTTP_404_NOT_FOUND)


class StockDailyPriceListView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        stock_daily_price = StockDailyPrice.objects.all()
        serializer = StockDailyPriceSerializer(stock_daily_price, many=True)
        return Response(serializer.data)


class StockDailyPriceView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, stock_code):
        stock_daily_price = StockDailyPrice.objects.filter(stock_code=stock_code).first()

        if stock_daily_price:
            serializer = StockDailyPriceSerializer(stock_daily_price)
            return Response(serializer.data)

        return Response({'error': 'Stock daily price information not found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = StockDailyPriceSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StockBalanceSheetListView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        stock_balance_sheet = StockBalanceSheet.objects.all()
        serializer = StockBalanceSheetSerializer(stock_balance_sheet, many=True)
        return Response(serializer.data)


class StockBalanceSheetView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, stock_code):
        stock_balance_sheet = StockBalanceSheet.objects.filter(stock_code=stock_code).first()

        if stock_balance_sheet:
            serializer = StockBalanceSheetSerializer(stock_balance_sheet)
            return Response(serializer.data)

        return Response({'error': 'Stock balance sheet information not found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = StockBalanceSheetSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StockCashFlowListView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        stock_cash_flow = StockCashFlow.objects.all()
        serializer = StockCashFlowSerializer(stock_cash_flow, many=True)
        return Response(serializer.data)


class StockCashFlowView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, stock_code):
        stock_cash_flow = StockCashFlow.objects.filter(stock_code=stock_code).first()

        if stock_cash_flow:
            serializer = StockCashFlowSerializer(stock_cash_flow)
            return Response(serializer.data)

        return Response({'error': 'Stock cash flow information not found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = StockCashFlowSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StockIncomeStatementListView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        stock_income_statement = StockIncomeStatement.objects.all()
        serializer = StockIncomeStatementSerializer(stock_income_statement, many=True)
        return Response(serializer.data)


class StockIncomeStatementView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, stock_code):
        stock_income_statement = StockIncomeStatement.objects.filter(stock_code=stock_code).first()

        if stock_income_statement:
            serializer = StockIncomeStatementSerializer(stock_income_statement)
            return Response(serializer.data)

        return Response({'error': 'Stock income statement information not found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = StockIncomeStatementSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
