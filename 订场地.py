
import datetime

# 存储所有预约信息的字典
# 格式: {(日期, 时间段, 场地号): 预约人姓名}
bookings = {}

# 营业时间段
TIME_SLOTS = [
    "09:00-10:00",
    "10:00-11:00",
    "11:00-12:00",
    "12:00-13:00",
    "13:00-14:00",
    "14:00-15:00",
    "15:00-16:00",
    "16:00-17:00",
    "17:00-18:00",
    "18:00-19:00",
    "19:00-20:00"
]

# 场地号
COURTS = list(range(1, 9))


def display_menu():
    """显示主菜单"""
    print("\n" + "=" * 40)
    print("      🏸 羽毛球场地预约系统 🏸")
    print("=" * 40)
    print("1. 预约场地")
    print("2. 查询场地是否可用")
    print("3. 查看所有已预约场地")
    print("4. 取消预约")
    print("0. 退出系统")
    print("=" * 40)


def get_valid_date():
    """获取有效的日期输入"""
    while True:
        date_str = input("请输入日期 (格式: YYYY-MM-DD): ").strip()
        try:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            if date < datetime.date.today():
                print("❌ 不能预约过去的日期，请重新输入。")
                continue
            return date_str
        except ValueError:
            print("❌ 日期格式错误，请按 YYYY-MM-DD 格式输入。")


def display_time_slots():
    """显示所有时间段"""
    print("\n可选时间段：")
    for i, slot in enumerate(TIME_SLOTS, 1):
        print(f"  {i}. {slot}")


def get_valid_time_slot():
    """获取有效的时间段选择"""
    display_time_slots()
    while True:
        try:
            choice = int(input("请选择时间段序号 (1-11): "))
            if 1 <= choice <= len(TIME_SLOTS):
                return TIME_SLOTS[choice - 1]
            else:
                print("❌ 请输入 1-11 之间的数字。")
        except ValueError:
            print("❌ 请输入有效的数字。")


def display_courts():
    """显示所有场地"""
    print("\n可选场地：")
    print("  场地号: 1  2  3  4  5  6  7  8")


def get_valid_court():
    """获取有效的场地选择"""
    display_courts()
    while True:
        try:
            court = int(input("请选择场地号 (1-8): "))
            if court in COURTS:
                return court
            else:
                print("❌ 请输入 1-8 之间的场地号。")
        except ValueError:
            print("❌ 请输入有效的数字。")


def check_availability(date, time_slot, court):
    """检查场地是否可用"""
    key = (date, time_slot, court)
    return key not in bookings


def book_court():
    """预约场地"""
    print("\n--- 预约场地 ---")
    
    # 获取预约信息
    date = get_valid_date()
    time_slot = get_valid_time_slot()
    court = get_valid_court()
    
    # 检查是否已被预约
    if not check_availability(date, time_slot, court):
        booker = bookings[(date, time_slot, court)]
        print(f"\n❌ 抱歉，{date} {time_slot} 场地 {court} 号已被 {booker} 预约。")
        return
    
    # 获取预约人姓名
    name = input("请输入预约人姓名: ").strip()
    if not name:
        print("❌ 姓名不能为空。")
        return
    
    # 确认预约信息
    print("\n" + "-" * 30)
    print("请确认预约信息：")
    print(f"  日期: {date}")
    print(f"  时间: {time_slot}")
    print(f"  场地: {court} 号")
    print(f"  预约人: {name}")
    print("-" * 30)
    
    confirm = input("确认预约？(Y/N): ").strip().upper()
    if confirm == 'Y':
        bookings[(date, time_slot, court)] = name
        print(f"\n✅ 预约成功！{date} {time_slot} 场地 {court} 号已为 {name} 预留。")
    else:
        print("\n⚠️ 已取消预约操作。")


def query_availability():
    """查询场地是否可用"""
    print("\n--- 查询场地可用性 ---")
    
    date = get_valid_date()
    time_slot = get_valid_time_slot()
    court = get_valid_court()
    
    if check_availability(date, time_slot, court):
        print(f"\n✅ {date} {time_slot} 场地 {court} 号 可以预约！")
    else:
        booker = bookings[(date, time_slot, court)]
        print(f"\n❌ {date} {time_slot} 场地 {court} 号 已被 {booker} 预约。")


def view_all_bookings():
    """查看所有已预约场地"""
    print("\n--- 所有已预约场地 ---")
    
    if not bookings:
        print("📋 暂无任何预约记录。")
        return
    
    # 按日期和时间排序
    sorted_bookings = sorted(bookings.items(), key=lambda x: (x[0][0], x[0][1], x[0][2]))
    
    print(f"\n{'日期':<12} {'时间段':<14} {'场地号':<8} {'预约人':<10}")
    print("-" * 50)
    
    current_date = None
    for (date, time_slot, court), name in sorted_bookings:
        if date != current_date:
            if current_date is not None:
                print("-" * 50)
            current_date = date
        print(f"{date:<12} {time_slot:<14} {court:<8} {name:<10}")
    
    print("-" * 50)
    print(f"共 {len(bookings)} 条预约记录。")


def cancel_booking():
    """取消预约"""
    print("\n--- 取消预约 ---")
    
    if not bookings:
        print("📋 暂无任何预约记录可取消。")
        return
    
    date = get_valid_date()
    time_slot = get_valid_time_slot()
    court = get_valid_court()
    
    key = (date, time_slot, court)
    
    if key not in bookings:
        print(f"\n❌ {date} {time_slot} 场地 {court} 号没有预约记录。")
        return
    
    booker = bookings[key]
    print(f"\n找到预约记录：{date} {time_slot} 场地 {court} 号，预约人：{booker}")
    
    confirm = input("确认取消此预约？(Y/N): ").strip().upper()
    if confirm == 'Y':
        del bookings[key]
        print(f"\n✅ 已成功取消 {date} {time_slot} 场地 {court} 号的预约。")
    else:
        print("\n⚠️ 已放弃取消操作。")


def main():
    """主程序"""
    print("\n欢迎使用羽毛球场地预约系统！")
    print("营业时间：每日 09:00 - 20:00，全年开放")
    print("可用场地：1-8 号场地")
    
    while True:
        display_menu()
        choice = input("请选择操作 (0-4): ").strip()
        
        if choice == '1':
            book_court()
        elif choice == '2':
            query_availability()
        elif choice == '3':
            view_all_bookings()
        elif choice == '4':
            cancel_booking()
        elif choice == '0':
            print("\n感谢使用，再见！🏸")
            break
        else:
            print("\n❌ 无效选择，请输入 0-4 之间的数字。")
        
        input("\n按 Enter 键返回主菜单...")


if __name__ == "__main__":
    main()
