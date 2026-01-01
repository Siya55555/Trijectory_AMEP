# Frontend Setup Instructions

## Prerequisites

- Node.js 18+ and npm
- VS Code (recommended)

## Installation

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Remove old node_modules and lock files (if exists):
```bash
rm -rf node_modules package-lock.json
# or on Windows
rmdir /s node_modules
del package-lock.json
```

3. Install dependencies:
```bash
npm install
```

4. Create `.env.local` file:
```bash
cp .env.example .env.local
```

5. Update `.env.local` if your backend is on a different URL:
```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api
```

6. Start development server:
```bash
npm run dev
```

## Expected Output

Frontend should be available at: `http://localhost:3000`

## Troubleshooting

### TypeScript Errors
- All JSX configuration errors should be resolved
- If issues persist, try clearing Next.js cache:
```bash
rm -rf .next
npm run dev
```

### Module Not Found
- Ensure all dependencies installed: `npm install`
- Clear node_modules and reinstall: `rm -rf node_modules && npm install`

### CORS Issues
- Ensure backend is running on `http://localhost:8000`
- Check CORS is enabled in `backend/main.py`

## Commands

```bash
npm run dev      # Start development server
npm run build    # Build for production
npm run start    # Start production server
npm run lint     # Run ESLint
```

Done! ✓
