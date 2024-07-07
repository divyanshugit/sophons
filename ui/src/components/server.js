const express = require('express');
const axios = require('axios');
const app = express();
const port = 8000;
const cors = require('cors');
const OpenAI = require('openai')

const corsOptions1 ={
    origin:'http://localhost:3000/chatbot', 
    credentials:true,            //access-control-allow-credentials:true
    optionSuccessStatus:200
}
app.use(cors(corsOptions1));
app.use(express.json());

app.post('/chat', async (req, res) => {
    try {
        const response = await axios.post('https://api.enkryptai.com/guardrails/detect', req.body, {
            headers: {
                'Content-Type': 'application/json',
                'api_key':'0fTJYGqUPn4n1ud8J1ammDEVFwNmepxY',
            }
        });
        res.json(response.data);
    } catch (error) {
        console.error('Error during API request:', error);
        res.status(500).json({ error: 'Error during API request' });
    }
});

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});
