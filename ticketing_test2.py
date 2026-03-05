import tkinter as tk
import json
import os

# Main application

class TicketApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Ticket System")

        # Data storage
        self.tickets = []
        self.ticket_counter = 1

        self.load_existing_tickets()

        # Frame container
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}

        # Register pages
        for F in (MainMenu, CreateTicket, LoadExistingTickets,
                  AddInvestigation, AddResolution,
                  AddCommunication, AddEvidence, CloseTicket):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenu)

    # Navigation

    def show_frame(self, page):
        self.frames[page].tkraise()

    # Persistence

    def save_tickets(self):
        with open("tickets.json", "w") as file:
            json.dump(self.tickets, file, indent=4)

    def load_existing_tickets(self):
        if os.path.exists("tickets.json"):
            try:
                with open("tickets.json", "r") as file:
                    self.tickets = json.load(file)

                if self.tickets:
                    self.ticket_counter = max(
                        ticket["ticket_id"] for ticket in self.tickets
                    ) + 1

            except json.JSONDecodeError:
                self.tickets = []
                self.ticket_counter = 1

        else:
            self.tickets = []
            with open("tickets.json", "w") as file:
                json.dump(self.tickets, file)

    #Ticket Logic

    def create_ticket(self, data):

        new_ticket = {
            "ticket_id": self.ticket_counter,
            "date_logged": data.get("date", ""),
            "time_logged": data.get("time", ""),
            "customer_name": data.get("customer_name", ""),
            "department": data.get("department", ""),
            "contact": data.get("contact", ""),
            "priority": data.get("priority", ""),
            "issue_category": data.get("issue_category", ""),
            "device_type": data.get("device_type", ""),
            "operating_system": data.get("operating_system", ""),
            "description": data.get("description", ""),
            "skill_level": data.get("skill_level", ""),
            "initial_diagnosis": data.get("diagnosis", ""),
            "investigation_steps": [],
            "actions_taken": [],
            "communication_log": [],
            "evidence_table": [],
            "performance_data": {},
            "status": "Open"
        }

        self.tickets.append(new_ticket)
        self.ticket_counter += 1

        self.save_tickets()

# GUI FRAMES (VIEWS)

class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        tk.Label(self, text="Main Menu").pack()

        tk.Button(self, text="Create Ticket",
                  command=lambda: controller.show_frame(CreateTicket)).pack()

        tk.Button(self, text="Load Existing Tickets",
                  command=lambda: controller.show_frame(LoadExistingTickets)).pack()

        tk.Button(self, text="Add Investigation",
                  command=lambda: controller.show_frame(AddInvestigation)).pack()

        tk.Button(self, text="Add Resolution",
                  command=lambda: controller.show_frame(AddResolution)).pack()

        tk.Button(self, text="Add Communication",
                  command=lambda: controller.show_frame(AddCommunication)).pack()

        tk.Button(self, text="Add Evidence",
                  command=lambda: controller.show_frame(AddEvidence)).pack()


# Create Ticket Page

class CreateTicket(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        tk.Label(self, text="Create Ticket").pack()

        tk.Button(self, text="Back",
                  command=lambda: controller.show_frame(MainMenu)).pack()


# Other Pages (Placeholder UI)

class LoadExistingTickets(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        tk.Label(self, text="Load Existing Tickets").pack()

        tk.Button(self, text="Back",
                  command=lambda: controller.show_frame(MainMenu)).pack()


class AddInvestigation(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        tk.Label(self, text="Add Investigation").pack()

        tk.Button(self, text="Back",
                  command=lambda: controller.show_frame(MainMenu)).pack()


class AddResolution(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        tk.Label(self, text="Add Resolution").pack()

        tk.Button(self, text="Back",
                  command=lambda: controller.show_frame(MainMenu)).pack()


class AddCommunication(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        tk.Label(self, text="Add Communication").pack()

        tk.Button(self, text="Back",
                  command=lambda: controller.show_frame(MainMenu)).pack()


class AddEvidence(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        tk.Label(self, text="Add Evidence").pack()

        tk.Button(self, text="Back",
                  command=lambda: controller.show_frame(MainMenu)).pack()


class CloseTicket(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        tk.Label(self, text="Close Ticket").pack()

        tk.Button(self, text="Back",
                  command=lambda: controller.show_frame(MainMenu)).pack()

# PROGRAM ENTRY

if __name__ == "__main__":
    app = TicketApp()
    app.mainloop()