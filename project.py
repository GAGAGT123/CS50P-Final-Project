import json
import os
from datetime import datetime

def main():
    """الوظيفة الرئيسية لتشغيل البرنامج"""
    tasks = load_tasks()
    
    while True:
        print("\n" + "="*50)
        print("📋 TASK MANAGER 📋")
        print("="*50)
        print("1. Add task")
        print("2. View all tasks")
        print("3. View pending tasks")
        print("4. View completed tasks")
        print("5. Complete task")
        print("6. Delete task")
        print("7. Exit")
        print("="*50)
        
        choice = input("\nChoose an option (1-7): ").strip()
        
        if choice == "1":
            task = add_task()
            tasks.append(task)
            save_tasks(tasks)
            print("✅ Task added successfully!")
            
        elif choice == "2":
            view_tasks(tasks, status="all")
            
        elif choice == "3":
            view_tasks(tasks, status="pending")
            
        elif choice == "4":
            view_tasks(tasks, status="completed")
            
        elif choice == "5":
            task_id = input("Enter task ID to complete: ")
            if complete_task(tasks, task_id):
                save_tasks(tasks)
                print("✅ Task completed!")
            else:
                print("❌ Invalid task ID!")
                
        elif choice == "6":
            task_id = input("Enter task ID to delete: ")
            if delete_task(tasks, task_id):
                save_tasks(tasks)
                print("🗑️ Task deleted!")
            else:
                print("❌ Invalid task ID!")
                
        elif choice == "7":
            print("👋 Goodbye!")
            break
            
        else:
            print("❌ Invalid choice! Please choose 1-7")


def add_task():
    """إضافة مهمة جديدة"""
    title = input("Task title: ").strip()
    while not title:
        title = input("Title cannot be empty! Task title: ").strip()
    
    description = input("Description (optional): ").strip()
    
    print("Priority options: high, medium, low")
    priority = input("Priority (default: medium): ").strip().lower()
    if priority not in ["high", "medium", "low"]:
        priority = "medium"
    
    task = {
        "id": None,
        "title": title,
        "description": description,
        "priority": priority,
        "status": "pending",
        "created_at": datetime.now().isoformat(),
        "completed_at": None
    }
    
    return task


def view_tasks(tasks, status="all"):
    """عرض المهام حسب الحالة"""
    if not tasks:
        print("📭 No tasks found!")
        return
    
    filtered_tasks = []
    for task in tasks:
        if status == "all":
            filtered_tasks.append(task)
        elif status == "pending" and task["status"] == "pending":
            filtered_tasks.append(task)
        elif status == "completed" and task["status"] == "completed":
            filtered_tasks.append(task)
    
    if not filtered_tasks:
        print(f"📭 No {status} tasks found!")
        return
    
    print(f"\n{'='*60}")
    print(f"📝 {status.upper()} TASKS ({len(filtered_tasks)})")
    print('='*60)
    
    for i, task in enumerate(filtered_tasks, 1):
        print(f"\n[{i}] ID: {task['id']}")
        print(f"    Title: {task['title']}")
        if task['description']:
            print(f"    Description: {task['description']}")
        print(f"    Priority: {get_priority_icon(task['priority'])} {task['priority']}")
        print(f"    Status: {task['status']}")
        print(f"    Created: {format_date(task['created_at'])}")
        if task['completed_at']:
            print(f"    Completed: {format_date(task['completed_at'])}")
        print("-"*40)


def complete_task(tasks, task_id):
    """تعليم مهمة كمكتملة"""
    for task in tasks:
        if task["id"] == task_id:
            if task["status"] == "completed":
                return False
            task["status"] = "completed"
            task["completed_at"] = datetime.now().isoformat()
            return True
    return False


def delete_task(tasks, task_id):
    """حذف مهمة"""
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(i)
            return True
    return False


def save_tasks(tasks):
    """حفظ المهام في ملف JSON"""
    try:
        for i, task in enumerate(tasks, 1):
            task["id"] = str(i)
        
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=2)
        print(f"💾 Saved {len(tasks)} tasks to file")
        return True
    except Exception as e:
        print(f"❌ Error saving tasks: {e}")
        return False


def load_tasks():
    """تحميل المهام من ملف JSON"""
    if os.path.exists("tasks.json"):
        try:
            with open("tasks.json", "r") as file:
                tasks = json.load(file)
                for i, task in enumerate(tasks, 1):
                    if task.get("id") is None:
                        task["id"] = str(i)
                print(f"✅ Loaded {len(tasks)} tasks from file")
                return tasks
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"⚠️ Error loading tasks: {e}")
            return []
    else:
        print("📭 No existing tasks file found. Starting fresh.")
        return []


def get_priority_icon(priority):
    """إرجاع أيقونة حسب الأولوية"""
    icons = {
        "high": "🔴",
        "medium": "🟡",
        "low": "🟢"
    }
    return icons.get(priority, "⚪")


def format_date(date_string):
    """تنسيق التاريخ للعرض"""
    try:
        date = datetime.fromisoformat(date_string)
        return date.strftime("%Y-%m-%d %H:%M")
    except:
        return date_string


if __name__ == "__main__":
    main()
