# TicketingSystem
A ticketing system for my IT Support Unit.

psudocode:

Main loop: 
BEGIN PROGRAM

    CALL load_existing_tickets

    DISPLAY main menu:
        1. Create New Ticket
        2. View Tickets
        3. Edit Ticket
        4. Add Investigation
        5. Add Resolution
        6. Add Communication Log
        7. Add Evidence
        8. Close Ticket
        9. Exit

END PROGRAM

Create tickets:
FUNCTION create_ticket

    CREATE new_ticket AS RECORD

    SET new_ticket.ticket_id TO ticket_counter
    SET new_ticket.date_logged TO current system date
    SET new_ticket.time_logged TO current system time

    INPUT customer_name
    INPUT department
    INPUT contact_details
    INPUT priority
    INPUT issue_category
    INPUT device_type
    INPUT operating_system

    INPUT customer_issue_description
    INPUT customer_skill_level
    INPUT technician_initial_diagnosis

    SET new_ticket.customer_name TO customer_name
    SET new_ticket.department TO department
    SET new_ticket.contact TO contact_details
    SET new_ticket.priority TO priority
    SET new_ticket.issue_category TO issue_category
    SET new_ticket.device_type TO device_type
    SET new_ticket.operating_system TO operating_system
    SET new_ticket.description TO customer_issue_description
    SET new_ticket.skill_level TO customer_skill_level
    SET new_ticket.initial_diagnosis TO technician_initial_diagnosis

    INITIALISE new_ticket.investigation_steps AS empty list
    INITIALISE new_ticket.actions_taken AS empty list
    INITIALISE new_ticket.communication_log AS empty list
    INITIALISE new_ticket.evidence_table AS empty list
    INITIALISE new_ticket.performance_data AS empty record
    INITIALISE new_ticket.reflection_section AS empty record

    SET new_ticket.status TO "Open"

    ADD new_ticket TO tickets list

    INCREMENT ticket_counter

    CALL save_tickets

END FUNCTION

Load Tickets:
FUNCTION load_existing_tickets

    IF "tickets.json" EXISTS THEN

        OPEN file FOR reading
        READ data
        CONVERT data TO tickets list
        CLOSE file

        IF tickets list IS NOT empty THEN
            SET ticket_counter TO (highest ticket_id in tickets) + 1
        ELSE
            SET ticket_counter TO 1
        ENDIF

    ELSE
        SET tickets TO empty list
        SET ticket_counter TO 1
    ENDIF

END FUNCTION

Investigation/Problem Identification:
FUNCTION add_investigation(ticket_id)

    FIND ticket WHERE ticket.ticket_id = ticket_id

    INPUT investigation_step
    INPUT tool_used
    INPUT screenshot_evidence

    CREATE investigation_record
        step = investigation_step
        tool = tool_used
        screenshot = screenshot_evidence

    ADD investigation_record TO ticket.investigation_steps

    CALL save_tickets

END FUNCTION

Resolution/Performance:
FUNCTION add_resolution(ticket_id)

    FIND ticket WHERE ticket.ticket_id = ticket_id

    INPUT actions_taken
    INPUT detailed_fix

    INPUT cpu_before
    INPUT cpu_after

    INPUT disk_before
    INPUT disk_after

    INPUT ram_before
    INPUT ram_after

    STORE all values IN ticket.performance_data

    SET ticket.status TO "Resolved"

    CALL save_tickets

END FUNCTION

Communications Log:
FUNCTION add_communication(ticket_id)

    FIND ticket WHERE ticket.ticket_id = ticket_id

    INPUT date
    INPUT method
    INPUT summary

    CREATE communication_record
        date = date
        method = method
        summary = summary

    ADD communication_record TO ticket.communication_log

    CALL save_tickets

END FUNCTION

Evidence:
FUNCTION add_evidence(ticket_id)

    FIND ticket WHERE ticket.ticket_id = ticket_id

    INPUT screenshot_number
    INPUT description
    INPUT problem_investigated
    INPUT resolution_description

    CREATE evidence_record
        screenshot_number = screenshot_number
        description = description
        problem = problem_investigated
        resolution = resolution_description

    ADD evidence_record TO ticket.evidence_table

    CALL save_tickets

END FUNCTION

Close Tickets:
FUNCTION close_ticket(ticket_id)

    FIND ticket WHERE ticket.ticket_id = ticket_id

    SET ticket.status TO "Closed"

    CALL save_tickets

END FUNCTION

Save Tickets:
FUNCTION save_tickets

    OPEN "tickets.json" FOR writing
    CONVERT tickets list TO JSON
    WRITE data TO file
    CLOSE file

END FUNCTION

