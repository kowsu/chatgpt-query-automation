import openai from 'openai';

const prompt = 'Hello, how can I help you today?';
const apiKey = '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';
const engineId = 'davinci';

openai.apiKey = apiKey;

openai.Completion.create({
    engine: engineId,
    prompt: prompt,
    maxTokens: 150,
    n: 1,
    stop: '\n',
}).then((response) => {
    const { choices } = response.data;
    const { text } = choices[0];
    console.log(text);
}).catch((error) => {
    console.log(error);
});
