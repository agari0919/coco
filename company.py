import matplotlib.pyplot as plt
import datetime

def create_company_graph(start_year, start_month, start_day):
    """
    創業年月日を起点とした企業ライフサイクルグラフを作成する。

    Args:
        start_year (int): 創業年
        start_month (int): 創業月
        start_day (int): 創業日
    """

    start_date = datetime.date(start_year, start_month, start_day)
    today = datetime.date.today()
    years = (today - start_date).days / 365

    # 平均的な企業のライフサイクルデータ（例）
    years_data = [0, 3, 10, 23.1]  # 創業、成長、成熟、倒産
    employees_data = [5, 50, 200, 10]  # 従業員数の推移（例）
    sales_data = [1000, 10000, 50000, 500]  # 年商の推移（万円）（例）

    # グラフ描画
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.plot(years_data, employees_data, marker='o')
    plt.title("従業員数の推移")
    plt.xlabel("創業からの年数")
    plt.ylabel("従業員数")

    plt.subplot(1, 2, 2)
    plt.plot(years_data, sales_data, marker='o')
    plt.title("年商の推移")
    plt.xlabel("創業からの年数")
    plt.ylabel("年商（万円）")

    plt.tight_layout()
    plt.show()

# 実行例
create_company_graph(2000, 4, 1)