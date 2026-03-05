import tkinter as tk
import os
import json

class TicketApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Ticket System")

        self.tickets = []
        self.ticket_counter = 1

        self.load_existing_tickets()

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}

        for F in (MainMenu, CreateTicket, LoadExistingTickets,
                  AddInvestigation, AddResolution,
                  AddCommunication, AddEvidence, CloseTicket):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenu)

    def show_frame(self, page):
        self.frames[page].tkraise()
        
    def save_tickets(self):
        with open("tickets.json", "w") as file:
            json.dump(self.tickets, file, indent=4)
        
    def create_ticket(self, data):

        new_ticket = {
        "ticket_id": self.ticket_counter,
        "date_logged": data["date"],
        "time_logged": data["time"],
        "customer_name": data["customer_name"],
        "department": data["department"],
        "contact": data["contact"],
        "priority": data["priority"],
        "issue_category": data["issue_category"],
        "device_type": data["device_type"],
        "operating_system": data["operating_system"],
        "description": data["description"],
        "skill_level": data["skill_level"],
        "initial_diagnosis": data["diagnosis"],
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

# The Main menu
class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Main Menu").pack()

        #Adds buttons to the menu
        tk.Button(self, text="Create Ticket",
                  command=lambda: controller.show_frame(CreateTicket)).pack()

        tk.Button(self, text="Load Existing Tickets",
                  command=lambda: controller.show_frame(LoadExistingTickets)).pack()
        
        tk.Button(self, text="Add Investigation",
                  command=lambda: controller.show_frame(AddInvestigation)).pack() 

#Adds the Create Ticket page.
class CreateTicket(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Create Ticket").pack()

        tk.Button(self, text="Back",
                  command=lambda: controller.show_frame(MainMenu)).pack()

#Adds the Load Existing Tickets page.
class LoadExistingTickets(tk.Frame):
    def __init__(self,parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Load Existing Tickets").pack()
        
#Adds the Add Investigation page.
class AddInvestigation(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Add Investigation").pack()

        tk.Button(self, text="Back",
                  command=lambda: controller.show_frame(MainMenu)).pack()
      
#Adds the Add Resolution page.  
class AddResolution(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Add Resolution").pack()

        tk.Button(self, text="Back",
                  command=lambda: controller.show_frame(MainMenu)).pack()

#Adds the Communication page.
class AddCommunication(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Add Communication").pack()

        tk.Button(self, text="Back",
                  command=lambda: controller.show_frame(MainMenu)).pack()
        
#Adds the Evidence page.
class AddEvidence(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Add Evidence").pack()

        tk.Button(self, text="Back",
                  command=lambda: controller.show_frame(MainMenu)).pack()

#Adds the close ticket page.
class CloseTicket(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Close Ticket").pack()

        tk.Button(self, text="Back",
                  command=lambda: controller.show_frame(MainMenu)).pack()
        
   
    def load_existing_tickets(self):
        if os.path.exists("tickets.json"):
            try:
                with open("tickets.json", "r") as file:
                    self.tickets = json.load(file)

                # Set ticket counter correctly
                if self.tickets:
                    self.ticket_counter = max(
                        ticket["ticket_id"] for ticket in self.tickets
                    ) + 1
                else:
                    self.ticket_counter = 1

            except json.JSONDecodeError:
                # If file is corrupted
                self.tickets = []
                self.ticket_counter = 1

        else:
            # Create empty file
            self.tickets = []
            with open("tickets.json", "w") as file:
                json.dump(self.tickets, file)



app = TicketApp()
app.mainloop()
