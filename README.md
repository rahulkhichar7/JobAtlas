# JobAtlas

A visual job application tracking system built around an interactive graph.

The application tracks companies, job opportunities, applications, and application progress while providing a separate interactive graph for each career category.

---

## Goals

- Track job opportunities across multiple companies.
- Organize companies into customizable categories.
- Track multiple roles for the same company.
- Track application status and progress.
- Maintain application history.
- Add notes and additional information to every relevant entity.
- Visualize applications as an interactive graph.
- Filter graphs by application status.
- Add, edit, and delete graph entities directly from the UI.
- Keep the backend and frontend separated.
- Follow proper Low-Level Design principles.
- Keep the system modular and easy to extend.

---

## Core Graph Structure

```text
Global
  │
  └── Category
        │
        └── Company
              │
              └── Job
                    │
                    └── Application
                          │
                          └── Progress
```

Progress nodes are optional and are created only when an application moves through additional stages.

---

## Main Entities

### Category

Represents a career/application category.

Examples:

- Software
- Quant
- Pharma
- Research
- Consulting

Categories should be dynamically configurable.

### Company

Stores information about a company.

Possible information:

- Name
- Category
- Website
- Location
- Description
- Notes

### Job

Represents a specific job opportunity.

Possible information:

- Job title
- Job type
- Location
- Job URL
- Date discovered
- Deadline
- Description
- Notes

### Application

Represents the user's application to a job.

Possible information:

- Application date
- Current status
- Priority
- Resume used
- Notes
- Next action
- Next action date

### Progress

Represents a stage reached after applying.

Examples:

- Online Assessment
- Technical Interview
- HR Interview
- Managerial Interview
- Offer

Progress should maintain historical information such as:

- Stage
- Date
- Notes
- Result

---

## Application Statuses

Initial statuses:

- Discovered
- Interested
- Applied
- On Hold
- Rejected
- Withdrawn
- Expired
- Offer

Application progress stages may additionally include:

- Online Assessment
- Interview
- Technical Interview
- HR Interview

The status system should remain extensible.

---

## Graph Features

- Global/root node
- Category-specific graphs
- Company nodes
- Job nodes
- Optional progress nodes
- Drag-and-drop nodes
- Zoom and pan
- Node selection
- Custom node designs
- Add-node controls
- Edit controls
- Delete controls
- Confirmation before deletion
- Automatic graph reconstruction after filtering
- Graph filtering by status
- Graph filtering by category
- Graph filtering by job type
- Graph filtering by company
- Graph filtering by date
- Graph filtering by priority

---

## Node Operations

### Global Node

Can add:

- Category
- Company

### Category Node

Can add:

- Company

### Company Node

Can add:

- Job

Can:

- Edit
- Delete

Deleting a company should also delete its dependent jobs, applications, and progress records.

### Job Node

Can:

- Edit
- Delete
- Add application/progress information

Deleting a job should delete its dependent application and progress records.

### Application Node

Can:

- Edit
- Delete
- Add progress

### Progress Node

Can:

- Edit
- Delete

All destructive operations require confirmation.

---

## Graph Filtering

Examples:

```text
Status

[ All ]
[ Active ]
[ Applied ]
[ Interview ]
[ Offer ]
[ Rejected ]
[ On Hold ]
[ Withdrawn ]
[ Expired ]
```

Additional filters:

```text
Category
Job Type
Company
Location
Priority
Date
```

The graph should be reconstructed from the filtered dataset.

---

## Dashboard

The dashboard will eventually contain:

- Total companies
- Total jobs
- Total applications
- Active applications
- Interviews
- Offers
- Rejections
- Response rate
- Interview rate
- Offer rate
- Upcoming deadlines
- Upcoming actions

---

## Application Timeline

Each application should maintain a history.

Example:

```text
18 Oct  → Applied
21 Oct  → Online Assessment
24 Oct  → Technical Interview
28 Oct  → HR Interview
02 Nov  → Offer
```

---

## Technology Stack

### Backend

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- SQLite
- Alembic

### Frontend

- React
- JavaScript/TypeScript
- React Flow
- HTML
- CSS

### Development

- Git
- GitHub
- Pytest
- ESLint
- Prettier

---

## Backend Architecture

```text
backend/
│
├── api/
│
├── models/
│
├── schemas/
│
├── services/
│
├── repositories/
│
├── database/
│
└── core/
```

Responsibilities:

```text
API
 ↓
Service
 ↓
Repository
 ↓
Database
```

Business logic should not be placed directly inside API endpoints.

---

## Frontend Architecture

```text
frontend/
│
├── pages/
├── components/
├── graph/
├── forms/
├── filters/
├── services/
├── hooks/
└── types/
```

The graph visualization should remain separate from business logic.

---

## Database

Initial database:

```text
SQLite
```

Potential future database:

```text
PostgreSQL
```

The application should use SQLAlchemy so that the database implementation can be changed with minimal impact on the rest of the system.

---

## Testing

Tests will cover:

- Database operations
- Repository operations
- Service logic
- API endpoints
- Validation
- Graph data generation
- Filtering
- Delete cascades

---

## Future Features

Possible future extensions:

- Authentication
- Multiple users
- Resume management
- Multiple resume versions
- Interview preparation
- Interview notes
- Application reminders
- Email integration
- Automatic email status detection
- Job scraping
- LinkedIn/job-board imports
- CSV import/export
- Analytics
- Application statistics
- Calendar integration
- Notifications
- PostgreSQL
- Cloud deployment

---

## Development Strategy

The application will be developed incrementally.

### Phase 1 — Project Setup

- Repository structure
- Python environment
- FastAPI
- React
- Database configuration

### Phase 2 — Database

- Category
- Company
- Job
- Application
- Progress

### Phase 3 — Backend

- Models
- Schemas
- Repositories
- Services
- API endpoints

### Phase 4 — Basic Frontend

- Dashboard
- Category pages
- Basic forms
- API integration

### Phase 5 — Graph

- Company nodes
- Job nodes
- Progress nodes
- Custom nodes
- Node connections

### Phase 6 — Graph Interaction

- Add
- Edit
- Delete
- Confirmation dialogs
- Node menus

### Phase 7 — Filtering

- Status
- Category
- Company
- Job type
- Date
- Priority

### Phase 8 — Application History

- Progress timeline
- Status history
- Notes
- Next actions

### Phase 9 — Analytics

- Response rate
- Interview rate
- Offer rate
- Application statistics

### Phase 10 — Advanced Features

- Notifications
- Resume management
- Email integration
- Job importing
- Deployment