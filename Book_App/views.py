
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Book
import traceback

#- logger 
import logging

#-- custmise logger 
logger = logging.getLogger("first")



# Create your views here.
#-- Business logic ----



def homepage(request):                                                      #-- httpRequest
    logger.info("In the home Page ...!")
    # print(request.method)
    # print(dir(request))
    # print(request.get_full_path())
    # print(request.get_full_path_info())
    print("In the Homepage")
    # a = 10
    # b = 5
    # res = a / b
    # print(res)
    # return HttpResponse(a)
    return render(request, "home.html")                                     #-- render is use to render the html page 
    # return HttpResponse("Welocome...!")                                   #-- httpResopence
    # return HttpResponse("Welocome...!\n<h1> Hi Hello </h2>") 


#--- Create the book  -----
def create_book(request):
    """ TO create the book """
    if request.method == "POST":
        logger.info("Create the book ...!")
        logger.info(request.POST)                                           #-- to get all data 
        if not request.POST.get("bid"):                                     #-- to edit the book
            book_name = request.POST["bname"]
            book_price = request.POST["bprice"]
            book_qut = request.POST["bqut"]
            Book.objects.create(Name=book_name, Price=book_price, qty=book_qut)
            return redirect("show_all_books")
        else:                                                                #--- to edit the book
            try:
                bid = request.POST.get("bid")
                book_obj = Book.objects.get(id=bid)
            except Exception as msg:
                logger.exception(msg)                                       #---- error in details
            book_obj.Name = request.POST["bname"]
            book_obj.Price = request.POST["bprice"]
            book_obj.qut = request.POST["bqut"]
            book_obj.save()
            return redirect("show_all_books")

    elif request.method == "GET":
        return render(request, "book_page.html")
    # return HttpResponse("Welcome to the book store")

 
#-- TO show all the boooks ---- 
def show_all_books(request):
    logger.info("In the Show all page .....!")
    try:
        all_books = Book.objects.all()                                 #--- to get all the book
    except Exception as msg:
        logger.exception(msg)
    else:
        logger.info(all_books)                                         #--- to get all the book in file and the consol
    return render(request, "show_all_books.html", {"books" : all_books})


#-- Edit book --
def edit_book(request, id):
    logger.info("Edit the book ....!")
    try:
        book = Book.objects.get(id=id)                                #--- to get the book from their id
    except Exception as msg:  
        logger.exception(msg)                                         #---- exception for get the complete error
    else:
        logger.info(book)                                             #---- to get the complete data those come for the edit
        return render(request, "book_page.html", {"book" : book})
        
    

#-- Delete book --
def delete_book(request, id):
    logger.info("Delete the book by their id.....!")
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist as err_msg:
        traceback.print_exc()                                         #--- trace back for shows the complete mas of the error -- need to import
    except Exception as msg:
        logger.exception(msg)
    else:
        book.delete()
        logger.info(book)                                            #---- to get the deleted book in the file and the consel
    return redirect("show_all_books")


#-- TO delete att the book
def delete_all_book(request):
    logger.info("Delete the all book .....!")
    try:
        all_book = Book.objects.all()
    except Exception as msg:
        logger.exception(msg)
    else:
        all_book.delete()
        logger.info(all_book)
        return redirect("show_all_books")


#-- Soft delete --
def soft_delete(request, id):
    logger.info("Soft deleted book by their id.....!")
    try:
        book = Book.objects.get(id=id)
        book.is_active = 0
        book.save()
        return redirect("show_all_books")
    except Exception as msg:
        logger.exception(msg)


#-- show all shoft delete book --
def show_soft_delete(request):
    logger.info("SHow all soft deleted book ....!")
    try:
        books = Book.objects.all().filter(is_active=0)
    except Exception as msg:
        logger.exception(msg)
    else:
        logger.info(books)
        return render(request, "soft_delete.html", {"books":books})     #--- when multiple books are thrir then s id manadtry other wise not shows the data    


#--- Restore the book  --- not show output
def restore_book(request):
    logger.info("Restore the soft deleted book .....!")
    b_name = request.POST["bname"]
    b_price = request.POST["bprice"]
    b_qty = request.POST["bqty"]
    if request.POST.get("bid"):
        try:
            book_obj = Book.objects.get(id=request.POST.get("bid"))
            book_obj.Name = b_name
            book_obj.Price = b_price
            book_obj.qty = b_qty
            # book_obj.create(Name=b_name, Price=b_price, qty=b_qty, is_active=1)
            book_obj.save()
            return redirect("book_page")
        except Book.DoesNotExist as msg:
            print(msg)
        except Exception as msg:
            logger.exception(msg)
    else:
        book = Book.objects.create(Name=b_name, Price=b_price, qty=b_qty, is_active=1)
        book.save()
        return redirect("book_page")













