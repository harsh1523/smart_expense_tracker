from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Expense
from .serializers import ExpenseSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def expenses_list_create(request):

    if request.method == 'GET':

        expenses = Expense.objects.filter(user=request.user)
        serializer = ExpenseSerializer(expenses, many=True)

        return Response(serializer.data)


    if request.method == 'POST':

        serializer = ExpenseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)

        return Response(serializer.errors)