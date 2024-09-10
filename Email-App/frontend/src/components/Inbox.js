import { useState, useEffect } from 'react';
import EmailItem from "./EmailItem";

export default function Inbox(props) {
	const [emails, setEmails] = useState([]);
	useEffect(() => {
		fetch('/email/retrieve/inbox').then(response => response.json()).then(res => setEmails(res));
	});
	return (
		<>
			{emails.map(email => <EmailItem key={email._id} email={email} setEmailId={props.setEmailId} add={'from'} />)}
		</>
	);
}
