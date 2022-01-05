import sys

# 初期設定
cash_balance = 0
e_money_balance = 0

cash_kind = [10,50,100,500,1000,5000,10000]
cash_numofsheet = [15,3,2,1,1,1,1]

cash_kind = [int(i) for i in cash_kind]
cash_numofsheet = [int(i) for i in cash_numofsheet]

cash_sum = [x * y for (x, y) in zip(cash_kind, cash_numofsheet)]

cash_balance = sum(cash_sum)

e_money_balance = 1000

#電子マネー関数
def e_money(payment_sum):
    global e_money_balance
    print('残高:',e_money_balance,'円')
    print('購入金額:',payment_sum,'円')
    yes_or_no = input('購入しますか？購入する場合は「1」を、キャンセルする場合は「2」を入力してください\n>>')
    if not yes_or_no.isdecimal():
        print('半角数字で入力してください。最初からやり直してください')
    elif yes_or_no == '1':
        e_money_balance = e_money_balance - payment_sum

        print('購入しました。電子マネー残高:',e_money_balance, '円')

        return e_money_balance

    elif yes_or_no == '2':
        print('キャンセルされました。最初からやり直してください')
    else:
        print('「1」か「2」を入力してください。最初からやり直してください。')

#券売機
while cash_balance > 130 or e_money_balance > 124:

    print('切符券売機です\n現金の場合130円、電子マネーの場合124円です\n現金で支払う場合は「1」を、電子マネーで支払う場合は「2」を半角で入力してください\n')
    print('プログラムを終了する場合は「3」を入力するか「Ctrl + C」で強制終了してください')

    payment_method = input('>>')

    if not payment_method.isdecimal(): #意図しない入力に対するエラー処理
        print('半角の数字で入力してください。最初からやり直してください')
        continue

    elif payment_method == '1': #現金支払いの場合
        print('現金支払いが選択されました。1枚あたり130円です\n')
        if cash_balance < 130:
            print('所持金が不足しています。他の支払い方法をご利用ください')
            continue 
        x = input('購入枚数を入力してください\n>>')
        if not x.isdecimal():
            print('半角数字で入力してください。最初からやり直してください')
        print('購入枚数:',x ,'枚')
        x = int(x)
        payment_sum = 130 * x
        print('購入金額',payment_sum, '円')
        if cash_balance < payment_sum:
            print('所持金が不足しているようです。最初からやり直してください。')
            continue
        yes_or_no = input('購入しますか？購入する場合は「1」を、キャンセルする場合は「2」を入力してください\n>>')
        if yes_or_no == '1':
            print('お金を投入してください')
            insert_cash = 0
            while payment_sum > insert_cash:
                insert_cash = 0
                cash_10 = input('10円玉の枚数 >>')
                if not cash_10.isdecimal:
                    print('半角の数字で入力してください。最初からやり直してください')
                cash_10 = int(cash_10)
                if cash_10 > cash_numofsheet[0]:
                    print('所持枚数が不足しています。最初からやり直してください。')
                    continue
                insert_cash = insert_cash + (10 * cash_10)

                cash_50 = input('50円玉の枚数 >>')
                if not cash_50.isdecimal:
                    print('半角の数字で入力してください。最初からやり直してください')
                cash_50 = int(cash_50)
                insert_cash = insert_cash + (50 * cash_50)

                cash_100 = input('100円玉の枚数 >>')
                if not cash_100.isdecimal:
                    print('半角の数字で入力してください。最初からやり直してください')
                cash_100 = int(cash_100)
                if cash_100 > cash_numofsheet[2]:
                    print('所持枚数が不足しています。最初からやり直してください。')
                    continue
                insert_cash = insert_cash + (100 * cash_100)

                cash_500 = input('500円玉の枚数 >>')
                if not cash_500.isdecimal:
                    print('半角の数字で入力してください。最初からやり直してください')
                cash_500 =+ int(cash_500)
                if cash_500 > cash_numofsheet[3]:
                    print('所持枚数が不足しています。最初からやり直してください。')
                    continue
                insert_cash = insert_cash + (500 * cash_500)

                cash_1000 = input('1000円札の枚数 >>')
                if not cash_1000.isdecimal:
                    print('半角の数字で入力してください。最初からやり直してください')
                cash_1000 = int(cash_1000)
                if cash_1000 > cash_numofsheet[4]:
                    print('所持枚数が不足しています。最初からやり直してください。')
                    continue
                insert_cash = insert_cash + (1000 * cash_1000)
                

                cash_5000 = input('5000円札の枚数 >>')
                if not cash_5000.isdecimal:
                    print('半角の数字で入力してください。最初からやり直してください')
                cash_5000 = int(cash_5000)
                if cash_5000 > cash_numofsheet[5]:
                    print('所持枚数が不足しています。最初からやり直してください。')
                    continue
                insert_cash = insert_cash + (5000 * cash_5000)

                cash_10000 = input('10000円札の枚数 >>')
                if not cash_10000.isdecimal:
                    print('半角の数字で入力してください。最初からやり直してください')
                cash_10000 = int(cash_10000)
                if cash_10000 > cash_numofsheet[6]:
                    print('所持枚数が不足しています。最初からやり直してください。')
                    continue
                insert_cash = insert_cash + (10000 * cash_10000)

                if insert_cash < payment_sum:
                    print('投入金額が不足しています。最初からやり直してください')
                    continue

            print('投入金額:', insert_cash,'円')

            cash_balance = cash_balance - insert_cash

            if cash_balance < 0:
                print('所持金が不足しています。最初からやり直してください')
                continue

            cash_numofsheet[0] = cash_numofsheet[0] - cash_10
            cash_numofsheet[1] = cash_numofsheet[1] - cash_50
            cash_numofsheet[2] = cash_numofsheet[2] - cash_100
            cash_numofsheet[3] = cash_numofsheet[3] - cash_500
            cash_numofsheet[4] = cash_numofsheet[4] - cash_1000
            cash_numofsheet[5] = cash_numofsheet[5] - cash_5000
            cash_numofsheet[6] = cash_numofsheet[6] - cash_10000
            
            change = insert_cash - payment_sum

            if change < 0:
                print('投入金額が不足しています。最初からやり直してください')
                continue

            print('お釣り:',change, '円')

            cash_balance = cash_balance + change

            change_5000 = change // 5000
            change = change % 5000
            change_1000 = change //1000
            change = change % 1000
            change_500 = change // 500
            change = change % 500
            change_100 = change // 100
            change = change % 100
            change_50 = change // 50
            change = change % 50
            change_10 = change // 10
            change = change % 10

            cash_numofsheet[0] = cash_numofsheet[0] + change_10
            cash_numofsheet[1] = cash_numofsheet[1] + change_50
            cash_numofsheet[2] = cash_numofsheet[2] + change_100
            cash_numofsheet[3] = cash_numofsheet[3] + change_500
            cash_numofsheet[4] = cash_numofsheet[4] + change_1000
            cash_numofsheet[5] = cash_numofsheet[5] + change_5000

            print('所持金残額:',cash_balance, '円')

            print('10円玉:',cash_numofsheet[0],'枚')
            print('50円玉:',cash_numofsheet[1],'枚')
            print('100円玉:',cash_numofsheet[2],'枚')
            print('500円玉:',cash_numofsheet[3],'枚')
            print('1000円札:',cash_numofsheet[4],'枚')
            print('5000円札:',cash_numofsheet[5],'枚')
            print('10000円札:',cash_numofsheet[6],'枚')

        elif yes_or_no == '2':
            print('キャンセルされました。最初からやり直してください\n')
        else:
            print('「1」か「2」を入力してください。最初からやり直してください\n')
        
    elif payment_method == '2': #電子マネー支払いの場合
        print('電子マネー払いが選択されました。1枚あたり124円です\n')
        x = input('購入枚数を半角数字で入力してください\n>>')
        if not x.isdecimal():
            print('半角数字で入力してください。最初からやり直してください')
        x = int(x)
        payment_sum = 124 * x
        if payment_sum > e_money_balance:
            print('残高不足です。最初からやり直してください。')
            continue
        e_money(payment_sum)
        continue
    elif payment_method == '3':
        print('プログラムを終了します')
        sys.exit()
    else: #意図しない入力に対するエラー処理
        print('「1」か「2」を入力してください。最初からやり直してください')
        continue

print('切符を購入できる所持金がないようです。またのご利用をおまちしております')